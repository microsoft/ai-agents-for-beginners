<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-30T10:24:49+00:00",
  "source_file": "11-agentic-protocols/code_samples/mcp-agents/README.md",
  "language_code": "my"
}
-->
# MCP ဖြင့် Agent-to-Agent ဆက်သွယ်မှုစနစ်များ တည်ဆောက်ခြင်း

> TL;DR - MCP တွင် Agent2Agent ဆက်သွယ်မှု တည်ဆောက်နိုင်ပါသလား? အတိအကျ - တည်ဆောက်နိုင်ပါတယ်!

MCP သည် "LLMs များအတွက် အကြောင်းအရာပေးခြင်း" ဆိုသည့် မူလရည်ရွယ်ချက်ထက် အလွန်တိုးတက်လာခဲ့ပါသည်။ [resumable streams](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling), နှင့် [progress](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) နှင့် [resources](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification) အကြောင်းကြားချက်များအပါအဝင် နောက်ဆုံးတိုးတက်မှုများဖြင့် MCP သည် အဆင့်မြင့် agent-to-agent ဆက်သွယ်မှုစနစ်များ တည်ဆောက်ရန် အခြေခံအုတ်မြစ်အား ပိုမိုခိုင်မာစေပါသည်။

## Agent/Tool အထင်မှား

Agentic လုပ်ဆောင်ချက်များ (ကြာရှည်လည်ပတ်မှု, အလယ်အလတ်တွင် ထပ်မံ input လိုအပ်နိုင်မှု စသည်တို့) ပါဝင်သော tools များကို စမ်းသပ်နေသော developer များအနက် MCP သည် မသင့်တော်ကြောင်း အထင်မှားမှုများ ရှိနေသည်။ အဓိကအကြောင်းရင်းမှာ MCP ၏ tools primitive မူလဥပမာများသည် ရိုးရှင်းသော request-response ပုံစံများကို အာရုံစိုက်ထားခြင်းကြောင့် ဖြစ်ပါသည်။

ဤအထင်မှားမှုသည် ယနေ့အခါ မသင့်လျော်တော့ပါ။ MCP specification သည် ကြာရှည်လည်ပတ်နိုင်သော agentic လုပ်ဆောင်ချက်များ တည်ဆောက်ရန် လိုအပ်သော အခွင့်အရေးများကို ဖြည့်ဆည်းထားသော capabilities များဖြင့် နောက်ဆုံးလများအတွင်း အလွန်တိုးတက်လာခဲ့ပါသည်။

- **Streaming & Partial Results**: လုပ်ဆောင်မှုအတွင်း အချိန်နှင့်တပြေးညီ အခြေအနေများကို update ပြုလုပ်ခြင်း
- **Resumability**: Client များ disconnect ဖြစ်ပြီးနောက် ပြန်လည်ဆက်သွယ်နိုင်ခြင်း
- **Durability**: Server restart ဖြစ်ပါက ရလဒ်များ မပျောက်ဆုံးခြင်း (ဥပမာ - resource links ဖြင့်)
- **Multi-turn**: လုပ်ဆောင်မှုအတွင်း interactive input များကို elicitation နှင့် sampling ဖြင့် ထည့်သွင်းနိုင်ခြင်း

ဤ features များကို ပေါင်းစပ်၍ MCP protocol ပေါ်တွင် အဆင့်မြင့် agentic နှင့် multi-agent application များကို တည်ဆောက်နိုင်ပါသည်။

အညွှန်းအနေဖြင့် agent ကို MCP server တွင် ရရှိနိုင်သော "tool" အဖြစ် ရည်ညွှန်းပါမည်။ ဤသည်မှာ MCP client ကို implement လုပ်ထားသော host application တစ်ခုရှိနေပြီး MCP server နှင့် session တစ်ခုကို တည်ဆောက်ကာ agent ကို ခေါ်နိုင်သည်ကို ဆိုလိုပါသည်။

## MCP Tool ကို "Agentic" ဖြစ်စေသော အချက်များ

Implementation ကို စတင်မပြုလုပ်မီ ကြာရှည်လည်ပတ်နိုင်သော agents များကို ပံ့ပိုးရန် လိုအပ်သော infrastructure capabilities များကို သတ်မှတ်ပါမည်။

> Agent ကို ကြာရှည်လည်ပတ်နိုင်သော autonomous လုပ်ဆောင်ချက်များ ပြုလုပ်နိုင်ပြီး အချိန်နှင့်တပြေးညီ feedback အပေါ် အခြေခံ၍ အကြိမ်ကြိမ် ပြင်ဆင်မှုများ လိုအပ်နိုင်သော အဆင့်မြင့်လုပ်ငန်းများကို လုပ်ဆောင်နိုင်သော entity အဖြစ် သတ်မှတ်ပါမည်။

### 1. Streaming & Partial Results

ရိုးရှင်းသော request-response ပုံစံများသည် ကြာရှည်လည်ပတ်မှု task များအတွက် မသင့်လျော်ပါ။ Agents များသည် အောက်ပါအချက်များကို ပံ့ပိုးရန် လိုအပ်ပါသည်။

- အချိန်နှင့်တပြေးညီ progress updates
- အလယ်အလတ်ရလဒ်များ

**MCP Support**: Resource update notifications သည် streaming partial results များကို enable ပြုလုပ်ပေမယ့် JSON-RPC ၏ 1:1 request/response model နှင့် မတူညီမှုများကို ရှောင်ရှားရန် သေချာစွာ design ပြုလုပ်ရန် လိုအပ်ပါသည်။

| Feature                    | Use Case                                                                                                                                                                       | MCP Support                                                                                |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Real-time Progress Updates | User သည် codebase migration task တစ်ခုကို request ပြုလုပ်သည်။ Agent သည် progress ကို stream ပြုလုပ်သည် - "10% - Analyzing dependencies... 25% - Converting TypeScript files... 50% - Updating imports..."          | ✅ Progress notifications                                                                  |
| Partial Results            | "Generate a book" task သည် partial results များကို stream ပြုလုပ်သည် - ၁) Story arc outline, ၂) Chapter list, ၃) အချိန်နှင့်တပြေးညီ ပြီးစီးသော chapter များ။ Host သည် inspection, cancellation, သို့မဟုတ် redirect ပြုလုပ်နိုင်သည်။ | ✅ Notifications ကို "extended" ပြုလုပ်၍ partial results ထည့်သွင်းနိုင်သည်။ PR 383, 776 အပေါ် အဆိုပြုချက်များကို ကြည့်ပါ။ |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>ပုံ 1:</strong> MCP agent သည် ကြာရှည်လည်ပတ်မှု task အတွင်း အချိန်နှင့်တပြေးညီ progress updates နှင့် partial results များကို host application သို့ stream ပြုလုပ်ပုံကို ဤ diagram တွင် ဖော်ပြထားသည်။
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

### 2. Resumability

Agents များသည် network interruption များကို သက်သာစွာ ကိုင်တွယ်နိုင်ရန် လိုအပ်ပါသည်။

- Client disconnect ဖြစ်ပြီးနောက် ပြန်လည်ဆက်သွယ်နိုင်ခြင်း
- Disconnect ဖြစ်သည့်နေရာမှ ဆက်လက်လုပ်ဆောင်နိုင်ခြင်း (message redelivery)

**MCP Support**: MCP StreamableHTTP transport သည် session resumption နှင့် message redelivery ကို session IDs နှင့် last event IDs ဖြင့် ပံ့ပိုးပေးပါသည်။ Server သည် client reconnect ဖြစ်ပါက event replays ပြုလုပ်ရန် EventStore ကို implement လုပ်ထားရန် လိုအပ်ပါသည်။  
Transport-agnostic resumable streams အပေါ် အဆိုပြုချက် (PR #975) ကိုလည်း community မှ စဉ်းစားနေပါသည်။

| Feature      | Use Case                                                                                                                                                   | MCP Support                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Resumability | Client disconnect ဖြစ်သည့်အချိန်တွင် ကြာရှည်လည်ပတ်မှု task တစ်ခုရှိနေသည်။ Client ပြန်လည်ဆက်သွယ်သည့်အခါ session သည် မျှော်လင့်ထားသော events များကို replay ပြုလုပ်ကာ seamless ဖြစ်စွာ ဆက်လက်လုပ်ဆောင်နိုင်သည်။ | ✅ StreamableHTTP transport with session IDs, event replay, and EventStore |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>ပုံ 2:</strong> MCP ၏ StreamableHTTP transport နှင့် event store သည် session resumption ကို seamless ဖြစ်စေသည့်ပုံကို ဤ diagram တွင် ဖော်ပြထားသည်။ Client disconnect ဖြစ်ပါက ပြန်လည်ဆက်သွယ်ပြီး မျှော်လင့်ထားသော events များကို replay ပြုလုပ်ကာ task ကို ဆက်လက်လုပ်ဆောင်နိုင်သည်။
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

### 3. Durability

ကြာရှည်လည်ပတ်မှု agents များသည် အခြေအနေတည်ငြိမ်မှုကို လိုအပ်ပါသည်။

- Server restart ဖြစ်ပါက ရလဒ်များ မပျောက်ဆုံးခြင်း
- Status ကို out-of-band မှ retrieve ပြုလုပ်နိုင်ခြင်း
- Sessions များအတွင်း progress tracking

**MCP Support**: MCP သည် tool calls အတွက် Resource link return type ကို ပံ့ပိုးပေးပါသည်။ ယနေ့အခါ tool တစ်ခုကို design ပြုလုပ်ကာ resource တစ်ခုကို ဖန်တီးပြီး resource link ကို ချက်ချင်း return ပြုလုပ်သည့် pattern ကို အသုံးပြုနိုင်ပါသည်။ Tool သည် background တွင် task ကို ဆက်လက်လုပ်ဆောင်ပြီး resource ကို update ပြုလုပ်နိုင်သည်။ Client သည် resource ၏ state ကို poll ပြုလုပ်ကာ partial သို့မဟုတ် full results ကို ရယူနိုင်သည် (server ပေးသော resource updates အပေါ် အခြေခံ၍) သို့မဟုတ် resource update notifications ကို subscribe ပြုလုပ်နိုင်သည်။

Resource များကို poll ပြုလုပ်ခြင်း သို့မဟုတ် updates များကို subscribe ပြုလုပ်ခြင်းသည် resources ကို စွမ်းအင်များစားစေပြီး scale တွင် အကျိုးသက်ရောက်မှုများရှိနိုင်သည်။ Webhooks သို့မဟုတ် triggers များကို server မှ client/host application သို့ update များကို အကြောင်းကြားရန် အသုံးပြုနိုင်မှုအပေါ် အဆိုပြုချက် (PR #992 အပါအဝင်) များကို community မှ စဉ်းစားနေပါသည်။

| Feature    | Use Case                                                                                                                                        | MCP Support                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Durability | Server crash ဖြစ်သည့်အချိန်တွင် data migration task တစ်ခုရှိနေသည်။ Results နှင့် progress သည် restart ဖြစ်ပါက မပျောက်ဆုံးဘဲ client သည် status ကို စစ်ဆေးကာ persistent resource မှ ဆက်လက်လုပ်ဆောင်နိုင်သည်။ | ✅ Resource links with persistent storage and status notifications |

ယနေ့အခါ tool တစ်ခုကို design ပြုလုပ်ကာ resource တစ်ခုကို ဖန်တီးပြီး resource link ကို ချက်ချင်း return ပြုလုပ်သည့် pattern သည် ရိုးရိုးဖြစ်နေပါသည်။ Tool သည် background တွင် task ကို ဆက်လက်လုပ်ဆောင်ကာ resource notifications များကို progress updates အဖြစ် သို့မဟုတ် partial results အဖြစ် ထုတ်ပေးကာ resource ၏ content ကို update ပြုလုပ်နိုင်သည်။

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>ပုံ 3:</strong> MCP agents များသည် persistent resources နှင့် status notifications ကို အသုံးပြုကာ server restart ဖြစ်ပါက ကြာရှည်လည်ပတ်မှု task များကို ဆက်လက်လုပ်ဆောင်နိုင်ပုံကို ဤ diagram တွင် ဖော်ပြထားသည်။
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

### 4. Multi-Turn Interactions

Agents များသည် လုပ်ဆောင်မှုအတွင်း အပို input များကို လိုအပ်နိုင်ပါသည်။

- လူ့ clarification သို့မဟုတ် အတည်ပြုချက်
- AI အကူအညီ
- Dynamic parameter ပြင်ဆင်မှု

**MCP Support**: Sampling (AI input အတွက်) နှင့် elicitation (လူ့ input အတွက်) ဖြင့် အပြည့်အဝ ပံ့ပိုးထားသည်။

| Feature                 | Use Case                                                                                                                                     | MCP Support                                           |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Multi-Turn Interactions | Travel booking agent သည် user မှ price confirmation ကို request ပြုလုပ်ပြီးနောက် AI ကို travel data ကို အကျဉ်းချုပ်ရန် request ပြုလုပ်ကာ booking transaction ကို ပြီးစီးစေသည်။ | ✅ Elicitation for human input, sampling for AI input |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>ပုံ 4:</strong> MCP agents များသည် လုပ်ဆောင်မှုအတွင်း လူ့ input ကို interactive အဖြစ် request ပြုလုပ်ခြင်း သို့မဟုတ် AI အကူအညီကို mid-execution မှာ request ပြုလုပ်ခြင်းဖြင့် complex workflows များကို ပံ့ပိုးပေးပုံကို ဤ diagram တွင် ဖော်ပြထားသည်။
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

## MCP တွင် ကြာရှည်လည်ပတ်မှု Agents များကို တည်ဆောက်ခြင်း - Code အကျဉ်းချုပ်

ဤဆောင်းပါး၏ အစိတ်အပိုင်းအနေဖြင့် [code repository](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents) တစ်ခုကို ပေးထားပြီး MCP Python SDK နှင့် StreamableHTTP transport ကို အသုံးပြုကာ session resumption နှင့် message redelivery ကို implement လုပ်ထားသော ကြာရှည်လည်ပတ်မှု agents များ၏ အပြည့်အစုံ implementation ကို ပါဝင်သည်။ Implementation သည် MCP capabilities များကို ပေါင်းစပ်ကာ sophisticated agent-like behaviors များ enable ပြုလုပ်ပုံကို ပြသထားသည်။

အထူးသဖြင့် server တွင် အဓိက agent tools နှစ်ခုကို implement လုပ်ထားသည်။

- **Travel Agent** - elicitation ဖြင့် price confirmation ကို simulate ပြုလုပ်သော travel booking service
- **Research Agent** - sampling ဖြင့် AI-assisted summaries ကို ပြုလုပ်သော research tasks

Agent နှစ်ခုစလုံးသည် အချိန်နှင့်တပြေးညီ progress updates, interactive confirmations, နှင့် full session resumption capabilities များကို ပြသထားသည်။

### အဓိက Implementation အကြောင်းအရာများ

Server-side agent implementation နှင့် client-side host handling ကို အောက်ပါ capabilities အလိုက် ဖော်ပြထားသည်။

#### Streaming & Progress Updates - လုပ်ဆောင်မှုအခြေအနေကို အချိန်နှင့်တပြေးညီ ပြသခြင်း

Streaming သည် ကြာရှည်လည်ပတ်မှု task များအတွင်း agent များကို အချိန်နှင့်တပြေးညီ progress updates ပေးနိုင်စေကာ user များကို task status နှင့် intermediate results များအကြောင်း သိရှိစေသည်။

**Server Implementation (agent သည် progress notifications ပေးပို့သည်):**

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

**Client Implementation (host သည် progress updates ကို လက်ခံသည်):**

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

#### Elicitation - User Input ကို Request ပြုလုပ်ခြင်း

Elicitation သည် agent များကို လုပ်ဆောင်မှုအတွင်း user input ကို request ပြုလုပ်နိုင်စေသည်။ ဤသည်သည် confirmations, clarifications, သို့မဟုတ် approvals အတွက် အရေးပါသည်။

**Server Implementation (agent သည် confirmation ကို request ပြုလုပ်သည်):**

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

**Client Implementation (host သည် elicitation callback ကို ပံ့ပိုးပေးသည်):**

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

#### Sampling - AI အကူအညီကို Request ပြုလုပ်ခြင်း

Sampling သည် agent များကို execution အတွင်း AI အကူအညီကို request ပြုလုပ်နိုင်စေသည်။ ဤသည်သည် လူ့-AI ပေါင်းစပ် workflows များ enable ပြုလုပ်သည်။

**Server Implementation (agent သည် AI အကူအညီကို request ပြုလုပ်သည်):**

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

**Client Implementation (host သည် sampling callback ကို ပံ့ပိုးပေးသည်):**

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

#### Resumability - Disconnections အတွင်း Session Continuity

Resumability သည် ကြာရှည်လည်ပတ်မှု agent tasks များကို client disconnect ဖြစ်ပါက ဆက်လက်လုပ်ဆောင်နိုင်စေသည်။ ဤသည်ကို event stores နှင့် resumption tokens ဖြင့် implement ပြုလုပ်ထားသည်။

**Event Store Implementation (server သည် session state ကို သိမ်းဆည်းထားသည်):**

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

**Client Metadata with Resumption Token (client သည် သိမ်းဆည်းထားသော state ကို အသုံးပြုကာ ပြန်လည်ဆက်သွယ်သည်):**

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

Host application သည် session IDs နှင့် resumption tokens များကို locally သိမ်းဆည်းထားပြီး existing sessions သို့ ပြန်လည်ဆက်သွယ်ကာ progress သို့မဟုတ် state မပျောက်ဆုံးစေရန် enable ပြုလုပ်သည်။

### Code Organization

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>ပုံ 5:</strong> MCP-based agent system architecture
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

**Key Files:**

- **`server/server.py`** - Travel နှင့် research agents များကို ပံ့ပိုးသော resumable MCP server
- **`client/client.py`** - Resumption support, callback handlers, နှင့် token management ပါဝင်သော interactive host application
- **`server/event_store.py`** - Session resumption နှင့် message redelivery ကို enable ပြုလုပ်သော event store implementation

## MCP တွင် Multi-Agent Communication သို့ တိုးချဲ့ခြင်း

အထက်ပါ implementation ကို multi-agent systems သို့ တိုးချဲ့ရန် host application ၏ intelligence နှင့် scope ကို တိုးမြှင့်နိုင်သည်။

- **Intelligent Task Decomposition**: Host သည် complex user requests များကို analysis ပြုလုပ်ကာ subtasks များကို specialized agents များအတွက် ခွဲ

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။