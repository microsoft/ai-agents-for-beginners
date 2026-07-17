# రిస్పాన్సెస్ API చీట్ షీట్ (Python + Azure OpenAI)

> క్రింద ఉన్న అన్ని స్నిపెట్లు `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` అని అనుకుంటాయి మరియు `client` ఇప్పటికే ఇనిషియలైజ్ అయి ఉంది (చూడండి client సెటప్).

## ప్రాథమిక అభ్యర్థన
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## క్లయింట్ సెటప్ — EntraID (సిఫార్సు చేయబడింది)
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## క్లయింట్ సెటప్ — API కీ
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## అసింక్ క్లయింట్ సెటప్ — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## అసింక్ క్లయింట్ సెటప్ — స్పష్టమైన టెనెంట్ తో EntraID (మల్టీ-టెనెంట్)

Azure OpenAI రిసోర్స్ డిఫాల్ట్ కంటే **వేరే టెనెంట్** లో ఉన్నప్పుడు, క్రెడెన్షియల్ కు `tenant_id` స్పష్టంగా అందించండి. ఇది అభివృద్ధి/పరీక్ష పరిస్థితుల్లో సాధారణం, ఇక్కడ డెవలపర్ హోమ్ టెనెంట్ రిసోర్స్ టెనెంట్ కంటే వేరు ఉంటుంది.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ఉత్పత్తి కోసం ManagedIdentityCredential (Azure కంటైనర్ ఆప్స్, ఆప్ సర్వీస్, మొదలైనవి)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # యూజర్-అయినmanaged شناخت
)
# స్థానిక డెవలప్‌మెంట్ కోసం AzureDeveloperCliCredential — స్పష్టమైన tenant_id అవసరం
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# చెయిన్: ముందుగా managed identity ప్రయత్నించండి, లేదంటే azd CLI కి వెళ్ళండి
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## అసింక్ క్లయింట్ మైగ్రేషన్ — ముందు/తరువాత

ముందు (పాతది):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

తర్వాత:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## పూర్తి సింక్రోనస్ మైగ్రేషన్ — ముందు/తరువాత

ముందు (పాత పద్ధతి — Azure OpenAI చాట్ కంప్లీషన్స్):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

తర్వాత (రిస్పాన్సెస్ API — Azure OpenAI v1 ఎండ్పాయింట్):
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## స్ట్రీమింగ్ (సింక్)
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # చివరలో నవ బైట్
```

## స్ట్రీమింగ్ (అసింక్)
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## వెబ్ అప్లికేషన్ స్ట్రీమింగ్ — బీకెండ్ నుండి ఫ్రంట్ ఎండ్ ఆకారం

SSE/JSONL ను ఫ్రంట్ ఎండ్ కు స్ట్రీమ్ చేసే వెబ్ అప్లికేషన్ మార్పిడి సమయంలో, **బీకెండ్ సీరియలైజేషన్ ఫార్మాట్** మారుతుంది. ఫ్రంట్ ఎండ్ ఇప్పటికే ఉన్న యాక్సెస్ ప్యాటర్న్స్ ని నిలుపుకునేలా కొత్త బీకెండ్ అవుట్‌పుట్ డిజైన్ చేయండి, తద్వారా ఫ్రంట్ ఎండ్లో ఎలాంటి మార్పులు అవసరం ఉండవు.

**ముందు** — చాట్ కంప్లీషన్స్ బీకెండ్ సాధారణంగా ప్రతి చంక్ యొక్క `choices[0]` డిక్ట్ ని సీరియలైజ్ చేస్తుంది:
```python
# పాతది: ప్రతి చంక్ ಗೆ సిరియలైజ్ చేయబడిన పూర్తి ఎంపిక డిక్షనరీ
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
ఫ్రంట్ ఎండ్ చదువుతుంది: `response.delta.content` (చాయిస్ ఆబ్జెక్ట్ లో లోతైన మార్గం).

**తరువాత** — రిస్పాన్సెస్ API బీకెండ్ ఒక కనిష్ట ఆకారం విడుదల చేస్తుంది అదే ఫ్రంట్ ఎండ్ యాక్సెస్ మార్గాన్ని నిలుపుకునే:
```python
# కొత్తది: ముందస్తు భాగం మాత్రమే అవసరం ఉంటే చెలామణీ చేయండి
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
ఫ్రంట్ ఎండ్ ఇంకా చదువుతుంది `response.delta.content` — **ఫ్రంట్ ఎండ్ లో ఎలాంటి మార్పులు అవసరం లేదు**.

> **ప్రధాన అవగాహన**: రిస్పాన్సెస్ API స్ట్రీమింగ్ ఆకారం (`event.type` + `event.delta`) చాట్ కంప్లీషన్స్ తో (`chunk.choices[0].delta.content`) మూలాధారంగా భిన్నమై ఉంటుంది. కానీ మీ బీకెండ్-టు-ఫ్రంట్ ఎండ్ ఒప్పందం మీరు నిర్వచించే విషయం. ఫ్రంట్ ఎండ్ ఇప్పటికే అంచనా వేసిన ఆకారాన్ని సరిపోల్చేలా బీకెండ్ అవుట్‌పుట్ రూపకల్పన చేయండి.

## స్ట్రీమింగ్ ఈవెంట్ క్రమం

`stream: true` ఉన్నప్పుడు, API ఈవెంట్లను ఈ క్రమంలో జారీ చేస్తుంది:
1. `response.created` – రిస్పాన్స్ ఆబ్జెక్ట్ ప్రారంభించబడింది
2. `response.in_progress` – జనరేషన్ ప్రారంభించబడింది
3. `response.output_item.added` – అవుట్‌పుట్ ఐటెం సృష్టించబడింది
4. `response.content_part.added` – కంటెంట్ భాగం ప్రారంభమైంది
5. `response.output_text.delta` – టెక్స్ట్ చంకులు (బహుళం, ప్రతి ఒక్కదీ `delta: string` కలిగి ఉంది)
6. `response.output_text.done` – టెక్స్ట్ జనరేషన్ పూర్తయింది
7. `response.content_part.done` – కంటెంట్ భాగం పూర్తి అయింది
8. `response.output_item.done` – అవుట్‌పుట్ ఐటెం పూర్తి అయింది
9. `response.completed` – సంపూర్ణ రిస్పాన్స్ పూర్తి అయింది

ప్రాథమిక టెక్స్ట్ స్ట్రీమింగ్ కోసం, కేవలం `response.output_text.delta` (టెక్స్ట్ చంకుల కోసం) మరియు `response.completed` (పూర్తి అయ్యింది) ని హ్యాండిల్ చేయండి.

## వెబ్ అప్లికేషన్లలో స్ట్రీమింగ్ లో తప్పుల నిర్వహణ

వెబ్ అప్లికేషన్ లో స్ట్రీమ్ చేసే సమయంలో, అసింక్ ఇటరేషన్ ను `try/except` తో కప్పండి మరియు తప్పులను JSON గా ఇచ్చి ఫ్రంట్ ఎండ్ వాటిని సుఖదాయకంగా ప్రదర్శించగలుగుతుంది (ఉదాహరణకు, రేట్ లిమిట్ లు, తాత్కాలిక తప్పులు):

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```

> **దీనికి కారణం ఏంటంటే**: Azure OpenAI రేట్ లిమిటింగ్ సమయంలో `429 Too Many Requests` తిరిగి ఇస్తుంది. `try/except` లేకుండా, స్ట్రీమింగ్ రిస్పాన్స్ నిశ్శబ్దంగా ముగుస్తుంది. దీనితో, ఫ్రంట్ ఎండ్ కి `{"error": "Too Many Requests"}` అందుతుంది మరియు పునఃప్రయత్న సూచన చూపించగలుగుతుంది.

## స్ట్రీమింగ్ ఈవెంట్ రకాలు (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## సంభాషణ ఫార్మాట్
```python
# రెస్పాన్సెస్ API ఇన్‌పుట్ అర్రే ద్వారా సంభాషణ ఫార్మాట్‌ను మద్దతు ఇస్తుంది
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## కంటెంట్ ఫిల్టర్ తప్పుల నిర్వహణ

తప్పుల బాడీ నిర్మాణం చాట్ కంప్లీషన్స్ నుండి రిస్పాన్సెస్ API కి మారింది.

ముందు (చాట్ కంప్లీషన్స్):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

తర్వాత (రిస్పాన్సెస్ API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ముఖ్య వ్యత్యాసాలు:
- `innererror` రాపర్ **తొలగించబడింది** — కంటెంట్ ఫిల్టర్ వివరాలు ఇప్పుడు `error.body` టాప్ లెవెల్ లో ఉంటాయి.
- `content_filter_result` (ఏకవచనం) → `content_filters` (బహువచనం సరసమయములో) ప్రతి ఎంట్రీలో `content_filter_results` (బహువచనం) కలిగి ఉంటుంది.
- ప్రతి `content_filters` ఎంట్రీలో `blocked`, `source_type`, మరియు `content_filter_results` ఉంటాయి, వాటిల్లో విభాగాలవారీ వివరాలు (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) ఉంటాయి.

సంపూర్ణ రిస్పాన్సెస్ API కంటెంట్ ఫిల్టర్ తప్పుల బాడీ ఆకారం:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## రా HTTP మైగ్రేషన్ (requests/httpx)

SDK ఉపయోగించకుండా అలంకారం Azure OpenAI REST ని నేరుగా పిలిచే అప్లికేషన్ ఉంటే:

ముందు (చాట్ కంప్లీషన్స్):
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

తర్వాత (రిస్పాన్సెస్ API):
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> **గమనిక**: `output_text` పేతనSDK లో `Response` ఆబ్జెక్టు పై సౌకర్యం గల ప్రాపర్టీ. రా REST JSON రిస్పాన్స్ కి టాప్-లెవెల్ `output_text` ఫీల్డ్ ఉండదు — టెక్స్ట్ `output[0].content[0].text` వద్ద ఉంటుంది.

## మల్టీ-టర్న్ సంభాషణ
```python
# Responses API తో సంభాషణని నిర్మించండి
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# సహాయకుని సమాధానాన్ని సంభాషణలో జోడించండి
messages.append({"role": "assistant", "content": response.output_text})

# సంభాషణను కొనసాగించండి
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

కంటెంట్-టైప్డ్ మల్టీ-టర్న్ (స్పష్టమైన `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ద్వారా మల్టీ-టర్న్ (వैकల్పికం)

సంభాషణ సరసమయమును మీరు స్వయంగా నిర్వహించకుండా, `previous_response_id` ఉపయోగించి సర్వర్-సైడ్ నుండి ప్రతిస్పందనలను చCHAIN చేయవచ్చు. API ప్రతి ప్రతిస్పందనని సંગ્રహించి
స్వయంచాలకంగా గత టర్న్స్ ముందు ఉంచుతుంది.


```python
# మొదటి మలుపు
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# తరువాతి మలుపులు — కొత్త వినియోగదారు సందేశం + గత స్పందన ID ను మాత్రమే పంపండి
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ఎప్పుడు ఏది ఉపయోగించాలి:**

| విధానం | లాభాలు | లోపాలు |
|---|---|---|
| `input` యారే (మాన్యువల్) | చరిత్రపై పూర్తిగా నియంత్రణ; ట్రిమ్/సారాంశం చేయవచ్చు; సర్వర్-సైడ్ నిల్వ అవసరం లేదు (`store=False`) | ఎక్కువ కోడ్; మీరు యారే ను నిర్వహిస్తారు |
| `previous_response_id` | సులభమైన కోడ్; ఆటోమ్యాటిక్ చైనింగ్ | `store=True` అవసరం (డిఫాల్ట్); సంభాషణ సర్వర్-సైడ్ నిల్వ అవుతుంది; టర్న్స్ మధ్య చరిత్రను మార్చలేరు |

> **మైగ్రేషన్ గమనిక:** ఎక్కువ చాట్ కంప్లీషన్స్ అప్లికేషన్లు ఇప్పటికే తమ స్వంత మెసేజ్ యారే ను నిర్వహిస్తాయి, అందువల్ల `input` యారే కి మార్పిడి మరింత ప్రత్యక్షమైన 1:1 మార్పిడి. కొత్త కోడ్ కి లేదా సంభాషణ చరిత్రను ప్రతిస్పందించాల్సిన అవసరం లేకపోతే `previous_response_id` ఉపయోగించండి.

## O-సిరీస్ రీజనింగ్ మోడల్స్ (o1, o3-mini, o3, o4-mini)

O-సిరీస్ మోడల్స్ కు Responses API కి మైగ్రేట్ చేసే సమయంలో ప్రత్యేక పారామెటర్ పరిమితులు ఉన్నాయి.

### o-సిరీస్ కోసం పారామెటర్ మ్యాపింగ్

| చాట్ కంప్లీషన్స్ (o-సిరీస్) | రిస్పాన్సెస్ API | గమనికలు |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | ఎక్కువగా సెట్ చేయండి (4096+) — తర్కం టోకెన్లు పరిమితికి వ్యతిరేకంగా లెక్కించబడతాయి |
| `reasoning_effort` | `reasoning.effort` | ఉన్నట్లుండి ఉంచండి (తక్కువ/మధ్యస్తం/ఎత్తైనది) |
| `temperature` | తీసివేయండి లేదా `1` గా సెట్ చేయండి | O-సిరీస్‌లో కేవలం `1` ని మాత్రమే అంగీకరిస్తుంది |
| `top_p` | తీసివేయండి | o-సిరీస్‌లో మద్దతు లేదు |
| `seed` | తీసివేయండి | Responses APIలో మద్దతు లేదు |

### O-సిరీస్ ముందు/తర్వాత

ముందు (o-సిరీస్‌తో చాట్ పూర్తి):  
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

తర్వాత (Responses API):  
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> **గమనిక**: O-సిరీస్ మోడల్స్ తర్క ప్రక్రియ సమయంలో అవుట్పుట్‌ను బఫర్ చేసి, టెక్స్ట్ డెల్టాను విడుదల చేసే ముందు ఇస్తాయి. స్ట్రీమింగ్ ఇంకా పనిచేస్తుంది కానీ మొదటి `response.output_text.delta` ఈవెంట్ GPT మోడల్స్‌తో పోలిస్తే ఎక్కువ ఆలస్యం తర్వాత వస్తుంది.

## తర్కం టోకెన్లకు యాక్సెస్
```python
# లాజిక్ మోడళ్లు అంతర్గత లాజిక్ ఉపయోగిస్తాయి — మీరు ఎంత స్థాయి లాజిక్ టోకెన్లు ఉపయోగించబడ్డాయో చూడవచ్చు
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> **ముఖ్యమైనది**: తర్కం మోడల్స్ అంతర్గత తర్క ప్రక్రియను పరిగణనలోకి తీసుకోవడం కోసం `max_output_tokens=1000` (50–200 కాదు) ఉపయోగించండి. మోడల్ తర్క టోకెన్లను అంతర్గతంగా ఉపయోగించి తుది అవుట్పుట్ ఉత్పత్తి చేస్తుంది.

## నిర్మిత అవుట్పుట్ — JSON స్కీమా
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## టూల్ ఉపయోగం

- `tools` లో ఫంక్షన్లను నిర్వచించండి **ఫ్లాట్ Responses API ఫార్మాట్** తో — టాప్ లెవల్లో `name`, `description`, మరియు `parameters` ఉండాలి (`function` కింద వద్దు).
- మోడల్ టూల్ కాల్ కోరినప్పుడు, తనిఖీ చేసి, తదుపరి అభ్యర్థనలో `input` లో `function_call_output` అంశంగా టూల్ ఫలితాన్ని చేర్చండి.
- స్కీమాలు కనిష్ఠంగా ఉంచండి; అమలు ముందు ఇన్పుట్‌లను నిర్ధారించండి.
- `strict: true` ఉపయోగించినప్పుడు, అన్ని ప్రాపర్టీలు `required` లో ఉచితంగా ఉండాలి, మరియు `additionalProperties: false` తప్పనిసరి.

> **⚠️ `pydantic_function_tool()` అనుకూలంగా లేదు**: `openai.pydantic_function_tool()` సహాయక సాధనం పాతచైతన్యపు అంతర్గత ఫార్మాట్ (`{"type": "function", "function": {"name": ...}}`) మాత్రమే ఉత్పత్తి చేస్తుంది. దాన్ని `responses.create()` తో ఉపయోగించవద్దు. టూల్ స్కీమాలను మానవీయంగా నిర్వచించండి లేదా అవుట్పుట్ ని ఫ్లాట్ చేయడానికి రాపర్ రాయండి.

### టూల్ నిర్వచన ఫార్మాట్

Responses API **ఫ్లాట్** టూల్ ఫార్మాట్ ఉపయోగిస్తుంది — `name`, `description`, `parameters` టాప్-లెవల్ కీలుగా ఉంటాయి (`function` కింద ఉండవు).

**ముందు (చాట్ పూర్తి — సారూప్య నిర్మాణం):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**తర్వాత (Responses API — ఫ్లాట్):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

పూర్తి ఉదాహరణ:  
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

`strict: true` తో (స్కీమా అమలు):  
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # అన్ని లక్షణాలు జాబితా చేయబడాలి
            "additionalProperties": False,   # కఠిన మోడ్ కోసం అవసరం
        },
    }
]
```

### టూల్ కాల్ సారి-సారి (నిర్వహించండి, ఫలితాలు తిరిగి ఇవ్వండి)

మోడల్ టూల్ కాల్ కోరినప్పుడు, `response.output` అంశాలు + `function_call_output` ఉపయోగించండి — **కాదు** చాట్ పూర్తి `role: assistant` + `role: tool` ప్యాటర్న్‌ను ఉపయోగించవద్దు.

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # model యొక్క function_call అంశాలను సంభాషణలో జోడించండి
    messages.extend(response.output)

    # ప్రతి సాధనాన్ని అమలు చేసి ఫలితాలను జోడించండి
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # సాధన ఫలితాలతో తుది స్పందన పొందండి
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### కొన్ని ఉదాహరణలతో టూల్ కాల్

`input` లో కొంచెం ఉదాహరణలు ఇచ్చేప్పుడు `function_call` మరియు `function_call_output` అంశాలు వాడండి. ఐడీలు `fc_` తో ప్రారంభమవాలి.

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# నిర్మిత వెబ్ శోధన ఉదాహరణ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## చిత్ర ఇన్‌పుట్

చిత్రం కంటెంట్ అంశాలు `image_url` నుండి `input_image` గా మారుతాయి, URL ఒక సారూప్య ఆబ్జెక్ట్ నుండి ఫ్లాట్ స్ట్రింగ్‌గా మారుతుంది.

### చిత్రం ఇన్‌పుట్ — ముందుగా (చాట్ పూర్తి)
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### చిత్రం ఇన్‌పుట్ — తరువాత (Responses API, URL)
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### చిత్రం ఇన్‌పుట్ — తరువాత (Responses API, base64)
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> **ముఖ్య మార్పులు**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (సారూప్య ఆబ్జెక్ట్) → `"image_url": "..."` (ఫ్లాట్ స్ట్రింగ్ — HTTPS URL లేదా `data:image/...;base64,...` డేటా URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) మార్పిడి

**మీ MAF సంస్కరణను ముందుగా తనిఖీ చేయండి** — మార్పిడి మీరు MAF 1.0.0+ లో ఉన్నారా లేక 1.0.0 కన్న ముందు బీటా/RC లో ఉన్నారాపై ఆధారపడి ఉంటుంది.

తనిఖీ చేయడానికి: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ లో, `OpenAIChatClient` **ఇప్పటికే Responses API ఉపయోగిస్తున్నది** — మార్పిడి అవసరం లేదు.

కోడ్‌బేస్ లెగาซి `OpenAIChatCompletionClient` (ఇది `chat.completions.create` ఉపయోగించింది) వాడితే, దీన్ని `OpenAIChatClient` తో మార్చండి:

ముందు:  
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

తర్వాత:  
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF 1.0.0 కన్న ముందు (బీటా/RC విడుదలలు)

1.0.0 కంటే ముందు MAF లో `OpenAIChatClient` చాట్ పూర్తి ఉపయోగించింది. `agent-framework-openai>=1.0.0` కి అప్‌డేట్ చేయండి, అక్కడ `OpenAIChatClient` Responses APIను డిఫాల్ట్‌గా ఉపయోగిస్తుంది.

> **గమనిక**: `Agent`, `MCPStreamableHTTPTool`, మరియు ఇతర MAF APIs మారవు — కేవలం క్లయింట్ క్లాస్ ఇంపోర్ట్ మరియు ఆబ్జెక్ట్ సృష్టి మారుతుంది.

## LangChain (`langchain-openai`) మార్పిడి

`ChatOpenAI()` లో `use_responses_api=True` జోడించండి. అలాగే మెసేజ్ కంటెంట్ యాక్సెస్‌ను `.content` నుండి `.text` కు మార్పు చేయండి.

ముందు:  
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... ఏజెంట్ పిలుపు ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

తర్వాత:  
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... ఏజెంట్ ఆహ్వానం ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **ముఖ్య మార్పులు**: (1) కన్‌స్ట్రక్టర్లో `use_responses_api=True`, (2) స్పందన సందేశాలలో `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->