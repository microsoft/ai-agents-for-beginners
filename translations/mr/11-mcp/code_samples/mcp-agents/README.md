<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-07-24T08:06:46+00:00",
  "source_file": "11-mcp/code_samples/mcp-agents/README.md",
  "language_code": "mr"
}
-->
# MCP वापरून एजंट-टू-एजंट संवाद प्रणाली तयार करणे

> TL;DR - MCP वर एजंट2एजंट संवाद तयार करू शकतो का? होय!

MCP ने "LLMs साठी संदर्भ प्रदान करणे" या मूळ उद्दिष्टापलीकडे लक्षणीय प्रगती केली आहे. [पुन्हा सुरू करता येणारे प्रवाह](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling), आणि सूचना ([प्रगती](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) आणि [संसाधने](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)) यांसारख्या अलीकडील सुधारणा MCP ला जटिल एजंट-टू-एजंट संवाद प्रणाली तयार करण्यासाठी एक मजबूत पाया प्रदान करतात.

## एजंट/टूल गैरसमज

जसजसे अधिक विकसक एजंटिक वर्तन असलेल्या साधनांचा (लांब कालावधीसाठी चालवणे, अंमलबजावणीच्या मध्यभागी अतिरिक्त इनपुटची आवश्यकता असणे इ.) शोध घेतात, तसतसे MCP अयोग्य असल्याचा एक सामान्य गैरसमज आहे, मुख्यतः कारण त्याच्या टूल्स प्रिमिटिव्हच्या सुरुवातीच्या उदाहरणांमध्ये साध्या विनंती-प्रतिसाद पद्धतींवर लक्ष केंद्रित केले होते.

हा दृष्टिकोन कालबाह्य झाला आहे. MCP स्पेसिफिकेशनमध्ये गेल्या काही महिन्यांत लक्षणीय सुधारणा करण्यात आल्या आहेत, ज्यामुळे लांब-चालणाऱ्या एजंटिक वर्तनासाठीची तफावत भरून निघाली आहे:

- **स्ट्रीमिंग आणि आंशिक निकाल**: अंमलबजावणी दरम्यान रिअल-टाइम प्रगती अद्यतने
- **पुन्हा सुरू करण्यायोग्यता**: क्लायंट डिस्कनेक्शननंतर पुन्हा कनेक्ट होऊ शकतो आणि सुरू ठेवू शकतो
- **टिकाऊपणा**: निकाल सर्व्हर रीस्टार्ट्सनंतर टिकून राहतात (उदा., संसाधन दुव्यांद्वारे)
- **मल्टी-टर्न**: अंमलबजावणीच्या मध्यभागी संवादात्मक इनपुट elicitation आणि sampling द्वारे

या वैशिष्ट्यांचा एकत्रितपणे वापर करून जटिल एजंटिक आणि मल्टी-एजंट अनुप्रयोग सक्षम केले जाऊ शकतात, जे सर्व MCP प्रोटोकॉलवर तैनात केले जातात.

संदर्भासाठी, आम्ही MCP सर्व्हरवर उपलब्ध असलेल्या "साधन" म्हणून एजंटचा उल्लेख करू. याचा अर्थ असा आहे की MCP क्लायंट अंमलबजावणी करणारे होस्ट अॅप्लिकेशन अस्तित्वात आहे, जे MCP सर्व्हरशी सत्र स्थापित करते आणि एजंटला कॉल करू शकते.

## MCP टूल "एजंटिक" काय बनवते?

अंमलबजावनीत जाण्यापूर्वी, लांब-चालणाऱ्या एजंट्सना समर्थन देण्यासाठी कोणत्या पायाभूत सुविधा क्षमतांची आवश्यकता आहे ते स्पष्ट करूया.

> आम्ही एजंटला अशा घटक म्हणून परिभाषित करू, जो विस्तारित कालावधीसाठी स्वायत्तपणे कार्य करू शकतो, ज्यामध्ये अनेक संवाद किंवा रिअल-टाइम अभिप्रायाच्या आधारे समायोजनांची आवश्यकता असलेल्या जटिल कार्यांना हाताळण्याची क्षमता आहे.

### 1. स्ट्रीमिंग आणि आंशिक निकाल

पारंपरिक विनंती-प्रतिसाद पद्धती लांब-चालणाऱ्या कार्यांसाठी कार्य करत नाहीत. एजंट्सना प्रदान करणे आवश्यक आहे:

- रिअल-टाइम प्रगती अद्यतने
- आंतरमधील निकाल

**MCP समर्थन**: संसाधन अद्यतन सूचना आंशिक निकालांचे प्रवाह सक्षम करतात, जरी JSON-RPC च्या 1:1 विनंती/प्रतिसाद मॉडेलशी संघर्ष टाळण्यासाठी काळजीपूर्वक डिझाइन आवश्यक आहे.

| वैशिष्ट्य                     | उपयोग प्रकरण                                                                                                                                                                       | MCP समर्थन                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| रिअल-टाइम प्रगती अद्यतने | वापरकर्ता कोडबेस स्थलांतर कार्याची विनंती करतो. एजंट प्रगती प्रवाहित करतो: "10% - अवलंबित्वांचे विश्लेषण करत आहे... 25% - टाइपस्क्रिप्ट फायली रूपांतरित करत आहे... 50% - आयात अद्यतनित करत आहे..."          | ✅ प्रगती सूचना                                                                  |
| आंशिक निकाल            | "पुस्तक तयार करा" कार्य आंशिक निकाल प्रवाहित करतो, उदा., 1) कथा चाप रूपरेषा, 2) अध्याय यादी, 3) प्रत्येक अध्याय पूर्ण झाल्याप्रमाणे. होस्ट तपासू शकतो, रद्द करू शकतो किंवा कोणत्याही टप्प्यावर पुनर्निर्देशित करू शकतो. | ✅ सूचना "विस्तारित" केल्या जाऊ शकतात, आंशिक निकालांचा समावेश करण्यासाठी PR 383, 776 वर प्रस्ताव पहा |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>आकृती 1:</strong> ही आकृती MCP एजंट कसे रिअल-टाइम प्रगती अद्यतने आणि आंशिक निकाल होस्ट अॅप्लिकेशनला प्रवाहित करतात हे दर्शवते, ज्यामुळे वापरकर्त्याला अंमलबजावणी रिअल-टाइममध्ये निरीक्षण करण्यास सक्षम करते.
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

### 2. पुन्हा सुरू करण्यायोग्यता

एजंट्सना नेटवर्क व्यत्ययांचा सहजतेने सामना करावा लागतो:

- (क्लायंट) डिस्कनेक्शननंतर पुन्हा कनेक्ट करा
- जिथे थांबले होते तिथून सुरू ठेवा (संदेश पुन्हा वितरित करणे)

**MCP समर्थन**: MCP StreamableHTTP ट्रान्सपोर्ट सत्र पुनरारंभ आणि संदेश पुन्हा वितरित करण्यासाठी सत्र IDs आणि शेवटच्या इव्हेंट IDs सह समर्थन करते. येथे महत्त्वाची गोष्ट म्हणजे सर्व्हरने इव्हेंट स्टोअर अंमलबजावणी करणे आवश्यक आहे, जे क्लायंट पुन्हा कनेक्शनवर इव्हेंट रीप्ले सक्षम करते.  
सामुदायिक प्रस्ताव (PR #975) ट्रान्सपोर्ट-अज्ञेय पुन्हा सुरू करण्यायोग्य प्रवाहांचा शोध घेत आहे.

| वैशिष्ट्य      | उपयोग प्रकरण                                                                                                                                                   | MCP समर्थन                                                                |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| पुन्हा सुरू करण्यायोग्यता | क्लायंट लांब-चालणाऱ्या कार्यादरम्यान डिस्कनेक्ट होतो. पुन्हा कनेक्शन केल्यावर, सत्र गमावलेल्या इव्हेंट्ससह पुन्हा सुरू होते, जिथे थांबले होते तिथून अखंडपणे सुरू राहते. | ✅ StreamableHTTP ट्रान्सपोर्ट सत्र IDs, इव्हेंट रीप्ले, आणि इव्हेंट स्टोअर सह |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>आकृती 2:</strong> ही आकृती दर्शवते की MCP च्या StreamableHTTP ट्रान्सपोर्ट आणि इव्हेंट स्टोअर सत्र पुनरारंभ कसे सक्षम करतात: जर क्लायंट डिस्कनेक्ट झाला, तर तो पुन्हा कनेक्ट होऊ शकतो आणि गमावलेले इव्हेंट रीप्ले करू शकतो, प्रगती गमावल्याशिवाय कार्य सुरू ठेवतो.
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

### 3. टिकाऊपणा

लांब-चालणाऱ्या एजंट्सना टिकाऊ स्थिती आवश्यक आहे:

- निकाल सर्व्हर रीस्टार्ट्सनंतर टिकून राहतात
- स्थिती बाहेरून मिळवता येते
- सत्रांमध्ये प्रगती ट्रॅकिंग

**MCP समर्थन**: MCP आता टूल कॉलसाठी संसाधन दुवा परतावा प्रकाराला समर्थन देते. आज, एक संभाव्य पद्धत म्हणजे संसाधन तयार करणारे टूल डिझाइन करणे आणि त्वरित संसाधन दुवा परत करणे. टूल पार्श्वभूमीत कार्य सुरू ठेवू शकते आणि संसाधन अद्यतनित करू शकते. याउलट, क्लायंट संसाधनाच्या स्थितीची स्थिती मिळवण्यासाठी निवडू शकतो, आंशिक किंवा पूर्ण निकाल मिळवू शकतो (सर्व्हर प्रदान करतो त्या संसाधन अद्यतनांवर आधारित) किंवा अद्यतन सूचना मिळवण्यासाठी संसाधनाची सदस्यता घेऊ शकतो.

येथे एक मर्यादा अशी आहे की संसाधने पोल करणे किंवा अद्यतनांसाठी सदस्यता घेणे संसाधने वापरू शकते, ज्याचा स्केलवर परिणाम होतो. वेबहुक्स किंवा ट्रिगर्स समाविष्ट करण्याच्या शक्यतेचा शोध घेणारा एक खुला सामुदायिक प्रस्ताव (यासह #992) आहे, ज्यामुळे सर्व्हर क्लायंट/होस्ट अॅप्लिकेशनला अद्यतनांची सूचना देऊ शकतो.

| वैशिष्ट्य    | उपयोग प्रकरण                                                                                                                                        | MCP समर्थन                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| टिकाऊपणा | सर्व्हर डेटा स्थलांतर कार्यादरम्यान क्रॅश होतो. निकाल आणि प्रगती रीस्टार्टनंतर टिकून राहते, क्लायंट स्थिती तपासू शकतो आणि टिकाऊ संसाधनातून सुरू ठेवू शकतो. | ✅ टिकाऊ संचयन आणि स्थिती अधिसूचनांसह संसाधन दुवे |

आज, एक सामान्य पद्धत म्हणजे संसाधन तयार करणारे टूल डिझाइन करणे आणि त्वरित संसाधन दुवा परत करणे. टूल पार्श्वभूमीत कार्य सुरू ठेवू शकते, संसाधन सूचना जारी करू शकते, ज्या प्रगती अद्यतन म्हणून काम करतात किंवा आंशिक निकालांचा समावेश करतात, आणि आवश्यकतेनुसार संसाधनातील सामग्री अद्यतनित करू शकते.

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>आकृती 3:</strong> ही आकृती दर्शवते की MCP एजंट्स टिकाऊ संसाधने आणि स्थिती अधिसूचना कशा वापरतात, याची खात्री करण्यासाठी की लांब-चालणारी कार्ये सर्व्हर रीस्टार्ट्सनंतर टिकून राहतात, ज्यामुळे क्लायंट प्रगती तपासू शकतो आणि अपयशानंतरही निकाल मिळवू शकतो.
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

### 4. मल्टी-टर्न संवाद

एजंट्सना अंमलबजावनीच्या मध्यभागी अतिरिक्त इनपुटची आवश्यकता असते:

- मानवी स्पष्टीकरण किंवा मान्यता
- जटिल निर्णयांसाठी AI सहाय्य
- डायनॅमिक पॅरामीटर समायोजन

**MCP समर्थन**: sampling (AI इनपुटसाठी) आणि elicitation (मानवी इनपुटसाठी) द्वारे पूर्णतः समर्थित.

| वैशिष्ट्य                 | उपयोग प्रकरण                                                                                                                                     | MCP समर्थन                                           |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| मल्टी-टर्न संवाद | प्रवास बुकिंग एजंट वापरकर्त्याकडून किंमत पुष्टीकरणाची विनंती करतो, नंतर बुकिंग व्यवहार पूर्ण करण्यापूर्वी प्रवास डेटा सारांशित करण्यासाठी AI ला विचारतो. | ✅ मानवी इनपुटसाठी elicitation, AI इनपुटसाठी sampling |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>आकृती 4:</strong> ही आकृती दर्शवते की MCP एजंट्स अंमलबजावनीच्या मध्यभागी संवादात्मक मानवी इनपुट किंवा AI सहाय्य कसे प्राप्त करू शकतात, पुष्टीकरणे आणि डायनॅमिक निर्णय घेण्यासारख्या जटिल, मल्टी-टर्न कार्यप्रवाहांना समर्थन देतात.
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

## MCP वर लांब-चालणारे एजंट्स अंमलबजावणी करणे - कोड विहंगावलोकन

या लेखाचा भाग म्हणून, आम्ही [कोड रिपॉझिटरी](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents) प्रदान करतो, ज्यामध्ये StreamableHTTP ट्रान्सपोर्टसह MCP Python SDK वापरून लांब-चालणाऱ्या एजंट्सची संपूर्ण अंमलबजावणी आहे. सत्र पुनरारंभ आणि संदेश पुन्हा वितरित करणे. अंमलबजावणी MCP क्षमतांचा एकत्रितपणे वापर करून प्रगत एजंटसारखे वर्तन सक्षम कसे करावे हे दर्शवते.

विशेषतः, आम्ही दोन प्राथमिक एजंट टूल्ससह सर्व्हर अंमलबजावितो:

- **प्रवास एजंट** - elicitation द्वारे किंमत पुष्टीकरणासह प्रवास बुकिंग सेवा अनुकरण करते
- **संशोधन एजंट** - sampling द्वारे AI-सहाय्यित सारांशांसह संशोधन कार्ये करते

दोन्ही एजंट्स रिअल-टाइम प्रगती अद्यतने, संवादात्मक पुष्टीकरणे आणि पूर्ण सत्र पुनरारंभ क्षमता दर्शवतात.

### मुख्य अंमलबजावणी संकल्पना

खालील विभाग प्रत्येक क्षमतेसाठी सर्व्हर-साइड एजंट अंमलबजावणी आणि क्लायंट-साइड होस्ट हाताळणी दर्शवतात:

#### स्ट्रीमिंग आणि प्रगती अद्यतने - रिअल-टाइम कार्य स्थिती

स्ट्रीमिंग एजंट्सना लांब-चालणाऱ्या कार्यांदरम्यान रिअल-टाइम प्रगती अद्यतने प्रदान करण्यास सक्षम करते, वापरकर्त्यांना कार्य स्थिती आणि आंतरमधील निकालांची माहिती ठेवते.

**सर्व्हर अंमलबजावणी (एजंट प्रगती सूचना पाठवतो):**

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

**क्लायंट अंमलबजावणी (होस्ट प्रगती अद्यतने प्राप्त करतो):**

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

#### elicitation - वापरकर्त्याच्या इनपुटची विनंती करणे

elicitation एजंट्सना अंमलबजावनीच्या मध्यभागी वापरकर्त्याच्या इनपुटची विनंती करण्यास सक्षम करते. हे लांब-चालणाऱ्या कार्यांदरम्यान पुष्टीकरणे, स्पष्टीकरणे किंवा मान्यता यासाठी आवश्यक आहे.

**सर्व्हर अंमलबजावणी (एजंट पुष्टीकरणाची विनंती करतो):**

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

**क्लायंट अंमलबजावणी (होस्ट elicitation callback प्रदान करतो):**

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

#### sampling - AI सहाय्याची विनंती करणे

sampling एजंट्सना अंमलबजावनी दरम्यान जटिल निर्णय किंवा सामग्री निर्मितीसाठी LLM सहाय्याची विनंती करण्यास सक्षम करते. हे हायब्रिड मानवी-AI कार्यप्रवाह सक्षम करते.

**सर्व्हर अंमलबजावणी (एजंट AI सहाय्याची विनंती करतो):**

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

**क्लायंट अंमलबजावणी (होस्ट sampling callback प्रदान करतो):**

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

#### पुन्हा सुरू करण्यायोग्यता - डिस्कनेक्शन दरम्यान सत्र सातत्य

पुन्हा सुरू करण्यायोग्यता सुनिश्चित करते की लांब-चालणारे एजंट कार्य क्लायंट डिस्कनेक्शन टिकून राहू शकतात आणि पुन्हा कनेक्शन केल्यावर अखंडपणे सुरू राहू शकतात. हे इव्हेंट स्टोअर्स आणि पुनरारंभ टोकनद्वारे अंमलबजावले जाते.

**इव्हेंट स्टोअर अंमलबजावणी (सर्व्हर सत्र स्थिती ठेवतो):**

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

**क्लायंट मेटाडेटा पुनरारंभ टोकनसह (क्लायंट साठवलेल्या स्थितीचा वापर करून पुन्हा कनेक्ट होतो):**

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

होस्ट अॅप्लिकेशन स्थानिकरित्या सत्र IDs आणि पुनरारंभ टोकन ठेवते, ज्यामुळे ते प्रगती किंवा स्थिती गमावल्याशिवाय विद्यमान सत्रांशी पुन्हा कनेक्ट होऊ शकते.

### कोड संघटना

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>आकृती 5:</strong> MCP-आधारित एजंट प्रणाली आर्किटेक्चर
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

**मुख्य फाइल्स:**

- **`server/server.py`** - प्रवास आणि संशोधन एजंट्ससह पुनरारंभ MCP सर्व्हर, जे elicitation, sampling, आणि प्रगती अद्यतने दर्शवतात
- **`client/client.py`** - पुनरारंभ समर्थन, callback हँडलर्स, आणि टोकन व्यवस्थापनासह संवादात्मक होस्ट अॅप्लिकेशन
- **`server/event_store.py`** - सत्र पुनरारंभ आणि संदेश पुन्हा

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.