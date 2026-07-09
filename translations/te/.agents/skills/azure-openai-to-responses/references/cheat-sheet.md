# స్పందనలు API చీట్ షీటు (పైథాన్ + అజ్యూర్ ఓపెన్ ఏఐ)

> క్రింది అన్ని సంకేతాలు `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` అని అనుకుంటాయి మరియు `client` ఇప్పటికే ప్రారంభించబడింది (క్లయింట్ సెటప్ చూడండి).

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

## క్లయింట్ సెటప్ — ఎంట్రాID (సిఫార్సు చేయబడింది)
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

## అసింక్ క్లయింట్ సెటప్ — ఎంట్రాID
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

## అసింక్ క్లయింట్ సెటప్ — ఎంట్రాID తో స్పష్టమైన అద్దింత (బహుళ అద్దింత)

అజ్యూర్ ఓపెన్ ఏఐ వనరు **వేరే అద్దింత** లో ఉన్నపుడు, ఆ ధృవీకరణకు `tenant_id` ను స్పష్టంగా పంపండి. ఇది సాధారణంగా డెవలపర్ ఇంటి అద్దింత వనరు అద్దింత కంటే వేరుగా ఉన్న dev/test సందర్భాలలో ఉంటుంది.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ఉత్పత్తి కోసం ManagedIdentityCredential (Azure కంటైనర్ యాప్స్, యాప్ సర్వీస్, మొదలైనవి)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # యూజర్-అసైన్ చేయబడిన మేనేజ్డ్ ఐడెంటిటీ
)
# స్థానిక డెవ్ కోసం AzureDeveloperCliCredential — స్పష్టమైన tenant_id చాలా అవసరం
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# చైన్: ముందుగా మేనేజ్డ్ ఐడెంటిటీను ప్రయత్నించండి, లేకపోతే azd CLI ని fallback చేయండి
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## అసింక్ క్లయింట్ మార్పిడి — ముందు/తరవాత

ముందు (పాత విధానం):
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4o",
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

## పూర్తి సమకాలిక మార్పిడి — ముందు/తరవాత

ముందు (పారంపరిక — అజ్యూర్ ఓపెన్ ఏఐ చాట్ కంప్లీషన్స్):
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

తర్వాత (స్పందనలు API — అజ్యూర్ ఓపెన్ ఏఐ v1 ఎండ్‌పాయింట్):
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

## స్ట్రీమింగ్ (సమకాలిక)
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
        print()  # చివరలో కొత్త పంక్తి
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

## వెబ్ యాప్ స్ట్రీమింగ్ — బ్యాక్‌ఎండ్ నుండి ఫ్రంటెండ్ ఆకారం

SSE/JSONL ని ఫ్రంటెండ్ కు స్ట్రీమ్ చేసే వెబ్ యాప్ మార్పిడి సమయంలో, **బ్యాక్‌ఎండ్ సిరియలైజేషన్ ఫార్మాట్** మారుతుంది. ఫ్రంటెండ్ కు ఎటువంటి మార్పులు అవసరం లేకుండా బ్యాక్‌ఎండ్ అవుట్‌పుట్ కొత్త ఆకారంలో ఉంటుందిగా డిజైన్ చేయండి.

**ముందు** — చాట్ కంప్లీషన్స్ బ్యాక్‌ఎండ్ సాధారణంగా ప్రతి చంక్ యొక్క `choices[0]` డిక్ట్‌ను సిరియలైజ్ చేసినది:
```python
# పాతది: చంక్‌ ప్రతి పూర్తి ఎంపిక డిక్షన్ సీరియలైజ్ చేయబడింది
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
ఫ్రంటెండ్ చదవడం: `response.delta.content` (చాయిస్ ఆబ్జెక్ట్ లో లోతైన మార్గం).

**తర్వాత** — స్పందనలు API బ్యాక్‌ఎండ్ కనిష్ట ఆకారాన్ని విడుదల చేస్తుంది, అదే ఫ్రంటెండ్ యాక్సెస్ మార్గం అన్‌చేంజ్డ్:
```python
# కొత్తది: ఫ్రంట్‌ఎండ్ అవసరమయ్యే దేన్ని మాత్రమే విడుదల చేయండి
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
ఫ్రంటెండ్ ఇప్పటికీ `response.delta.content` చదవుతుంది — **ఫ్రంటెండ్ లో ఎటువంటి మార్పులు అవసరం இல்லை**.

> **ముఖ్య అవగాహన**: స్పందనలు API స్ట్రీమింగ్ షేప్ (`event.type` + `event.delta`) చాట్ కంప్లీషన్స్ (`chunk.choices[0].delta.content`) నుండి మూలానికి భిన్నం. కానీ మీ బ్యాక్‌ఎండ్-ఫ్రంటెండ్ ఒప్పందం మీది. ఫ్రంటెండ్ ఇప్పటికే ఆశించే ఆకారానికి బ్యాక్‌ఎండ్ అవుట్‌పుట్ ఆకారాన్ని సరిపోల్చండి.

## స్ట్రీమింగ్ ఈవెంట్ క్రమం

`stream: true` ఉన్నప్పుడు, API ఈ ఈవెంట్లను ఈ క్రమంలో విడుదల చేస్తుంది:
1. `response.created` – స్పందన ఆబ్జెక్ట్ ప్రారంభమైంది
2. `response.in_progress` – జనరేషన్ ప్రారంభమైంది
3. `response.output_item.added` – అవుట్‌పుట్ అంశం సృష్టించబడింది
4. `response.content_part.added` – కంటెంట్ భాగం ప్రారంభమైంది
5. `response.output_text.delta` – టెక్స్ట్ చంక్లు (చాల్లగా, ప్రతి ఒక్కటికి `delta: string` ఉంటుంది)
6. `response.output_text.done` – టెక్స్ట్ జనరేషన్ పూర్తయింది
7. `response.content_part.done` – కంటెంట్ భాగం ముగిసింది
8. `response.output_item.done` – అవుట్‌పుట్ అంశం పూర్తయింది
9. `response.completed` – పూర్తి స్పందన పూర్తి

ప్రాథమిక టెక్స్ట్ స్ట్రీమింగ్ లో, కేవలం `response.output_text.delta` (టెక్స్ట్ చంక్ల కోసం) మరియు `response.completed` (ముగింపు కోసం) ను హ్యాండిల్ చేయండి.

## వెబ్ యాప్స్‌లో స్ట్రీమింగ్ లో తప్పిద హ్యాండ్లింగ్

వెబ్ యాప్‌లో స్ట్రీమింగ్ చేస్తున్నప్పుడు, అసింక్ ఇటనరేషన్‌ని `try/except` లో ముట్టడి చేసి పొరపాట్లు JSON గా ఫ్రంటెండ్‌కు అందించండి, ఫ్రంటెండ్ వాటిని శ్రద్ధగా చూపించగలుగుతుంది (ఉదాహరణకు, రేట్ లిమిట్స్, తాత్కాలిక వైఫల్యాలు):

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

> **ఇది ఎందుకు ముఖ్యమైనది**: అజ్యూర్ ఓపెన్ ఏఐ రేట్ లిమిటింగ్ సమయంలో `429 Too Many Requests` ను తిరిగి ఇస్తుంది. `try/except` లేకపోతే, స్ట్రీమింగ్ స్పందన నిశ్శబ్దంగా మృత్యువు అవుతుంది. దీని తో, ఫ్రంటెండ్ `{"error": "Too Many Requests"}` అందుకుంటుంది మరియు రీట్రై సూచన చూపించవచ్చు.

## స్ట్రీమింగ్ ఈవెంట్ రకాల (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## సంభాషణ ఫార్మాట్
```python
# ప్రతిస్పందనలు API ఇన్‌పుట్ అరేః ద్వారా సంభాషణ ఫార్మాట్‌కు మద్దతు ఇస్తుంది
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

## కంటెంట్ ఫిల్టర్ లోపం నిర్వహణ

లోపం టెంప్లేట్ చాట్ కంప్లీషన్స్ నుండి స్పందనలు API వరకు మారింది.

ముందు (చాట్ కంప్లీషన్స్):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

తర్వాత (స్పందనలు API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

ప్రధాన తేడాలు:
- `innererror` రాపపర్ **లేకుండా పోయింది** — కంటెంట్ ఫిల్టర్ వివరాలు ఇప్పుడు `error.body` యొక్క టాప్ లెవెల్లో ఉన్నాయి.
- `content_filter_result` (ఏకవచనం) → `content_filters` (బహువచనం అర్రేఅ) అందులో ప్రతి ఎంట్రీలో `content_filter_results` ఉన్నాయి.
- ప్రతి ఎంట్రీ `content_filters` లో `blocked`, `source_type`, మరియు `content_filter_results` ని పర్-కేటగిరీ వివరాలతో (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) కలిగి ఉంటుంది.

పూర్తి స్పందనలు API కంటెంట్ ఫిల్టర్ లోపం బాడీ ఆకారం:
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

యాప్ SDK ఉపయోగించకుండా నేరుగా అజ్యూర్ ఓపెన్ ఏఐ REST కు కాల్ చేస్తే:

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

తర్వాత (స్పందనలు API):
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

> **గమనిక**: `output_text` అనేది పైథాన్ SDKలోని `Response` ఆబ్జెక్ట్‌పై సౌకర్యమేలైన ప్రాపర్టీ. రా REST JSON స్పందనలో ఎటువంటి టాప్-లెవెల్ `output_text` ఫీల్డ్ లేదు — టెక్స్ట్ `output[0].content[0].text` వద్ద ఉంటుంది.

## బహుళ-తిరుగుడు సంభాషణ
```python
# Responses API తో సంభాషణను నిర్మించండి
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# అసిస్టెంట్ యొక్క స్పందనను సంభాషణలో జోడించండి
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

కంటెంట్-రకం బహుళ-తిరుగుడు (స్పష్టమైన `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ద్వారా బహుళ-తిరుగుడు (వికల్పం)

మీరు స్వయంగా సంభాషణ అర్రే నిర్వహించకుండా, మీరు సమాధానాలను `previous_response_id` ఉపయోగించి సర్వర్-మరుపై షైన్ చేయవచ్చు. API ప్రతి స్పందనను నిల్వచేసి
గత టర్న్స్ ను స్వయంచాలకంగా మొదట పెట్టుతుంది.


```python
# మొదటి తిప్ప
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# తరువాత తిప్పలు — కొత్త వినియోగదారు సందేశం + గత సమాధాన ID ని మాత్రమే పంపండి
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**ఏది ఎప్పుడు ఉపయోగించాలి:**

| పద్ధతి | లాభాలు | నష్టాలు |
|---|---|---|
| `input` అర్రే (మాన్యువల్) | ఇటివల చరిత్రపై పూర్తి నియంత్రణ; త్రిమ్ / సారాంశం చేయవచ్చు; సర్వర్-మరుపు అవసరం లేదు (`store=False`) | కోడ్ కొంత ఎక్కువ; మీరు అర్రే నిర్వహించాలి |
| `previous_response_id` | సులభమైన కోడ్; స్వయంచాలకమైన చైన్ చేన్ | `store=True` అవసరం (డిఫాల్ట్); సంభాషణ సర్వర్-పక్కన నిల్వ; టర్న్ల మధ్య చరిత్ర మార్పులు చేయలేరు |

> **మైగ్రేషన్ గమనిక:** చాలా చాట్ కంప్లీషన్స్ యాప్స్ ఇప్పటికే తమ సందేశ అర్రేను నిర్వహిస్తాయి, కాబట్టి `input` అర్రేనికి మారడం నేరుగా 1:1 మార్పిడి. కొత్త కోడ్ కోసం లేదా సంభాషణ చరిత్రను మార్చాల్సిన అవసరం లేనప్పుడు `previous_response_id` ఉపయోగించండి.

## O-సిరీస్ తార్కిక నమూనాలు (o1, o3-mini, o3, o4-mini)

O-సిరీస్ నమూనాలు స్పందనలు API కి మార్పిడి సమయంలో ప్రత్యేక పారామీటర్ పరిమితులు కలిగి ఉంటాయి.

### o-సిరీస్ కొరకు పారామీటర్ మ్యాపింగ్

| చాట్ కంప్లీషన్స్ (o-సిరీస్) | స్పందనలు API | గమనికలు |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | అధికంగా సెట్చేయండి (4096+) — తార్కిక టోకెన్లు పరిమితిలో చేర్చబడతాయి |
| `reasoning_effort` | `reasoning.effort` | ఉంటే అలాగే ఉంచండి (తక్కువ/మధ్యస్థ/అధిక) |
| `temperature` | తీసివేయండి లేదా `1` కి సెట్చేయండి | O-సిరీస్ మోడల్స్ కేవలం `1` ను అంగీకరిస్తాయి |
| `top_p` | తీసివేయండి | o-సిరీస్ వద్ద మద్దతు లేదు |
| `seed` | తీసివేయండి | స్పందనలు API లో మద్దతు లేదు |

### O-సిరీస్ ముందు/తర్వాత

ముందు (చాట్ కంప్లీషన్స్ తో o-సిరీస్):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

తర్వాత (స్పందనలు API):
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

> **గమనిక**: O-సిరీస్ మోడల్స్ తార్కికాసక్తి సమయంలో అవుట్‌పుట్ ని నిల్వ చేయవచ్చు, ఆ తర్వాత టెక్స్ట్ డెల్టాలను విడుదల చేస్తాయి. స్ట్రీమింగ్ పనిచేస్తుంది కానీ మొదటి `response.output_text.delta` ఈవెంట్ GPT మోడల్స్ కంటే ఎక్కువ ఆలస్యం తో రావచ్చు.

## తార్కిక టోకెన్లను యాక్సెస్ చేయడం
```python
# తర్కం మోడల్స్ అంతర్గత తర్కాన్ని ఉపయోగిస్తాయి — మీరు ఎంత తర్క టోకెన్లు ఉపయోగించబడ్డాయో చూడవచ్చు
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

> **ముఖ్యమైనది**: తార్కిక మోడల్స్ యొక్క అంతర్గత తార్కిక ప్రక్రియను పరిగణలోకి తీసుకుని `max_output_tokens=1000` ఉపయోగించండి (50–200 కాదు). మోడల్ తార్కిక టోకెన్లను అంతర్గతంగా ఉపయోగిస్తుంది ఫైనల్ అవుట్‌పుట్ రూపొందించే ముందు.

## నిర్మిత అవుట్‌పుట్ — JSON స్కీమా
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

## టూల్ ఉపయోగము

- **ఫ్లాట్ స్పందనలు API ఫార్మాట్ లో** `tools`‌లో ఫంక్షన్లు నిర్వచించండి — `name`, `description`, మరియు `parameters` టాప్ లెవెల్లో ఉండాలి (ఫంక్షన్ కింద మరియాదలేవు).
- మోడల్ టూల్ కాల్ అడిగినప్పుడు, మీ యాప్ లో దాన్ని నడుపండి మరియు తదుపరి అభ్యర్థనలో `input` లో `function_call_output` అంశంగా టూల్ ఫలితాన్ని చేర్చండి.
- స్కీమాలు కనిష్టంగా ఉంచండి; అమలు ముందు ఇన్‌పుట్లను ధ్రువీకరించండి.
- `strict: true` ఉపయోగించినప్పుడు, అన్ని ప్రాపర్టీలు `required`లో ఉండాలి మరియు `additionalProperties: false` అనివార్యం.

> **⚠️ `pydantic_function_tool()` అనుకూలం కాదు**: `openai.pydantic_function_tool()` సహాయకుడు పాత చాట్ కంప్లీషన్స్ సంక్లిష్ట ఫార్మాట్ (`{"type": "function", "function": {"name": ...}}`)ను ఇంకా ఉత్పత్తి చేస్తుంది. దీన్ని `responses.create()` తో ఉపయోగించవద్దు. టూల్ స్కీమాలు మాన్యువల్‌గా నిర్వచించండి లేదా అవుట్‌పుట్ ను ఫ్లాటన్ చేసే రాపర్ వ్రాయండి.

### టూల్ నిర్వచన ఫార్మాట్

స్పందనలు API **ఫ్లాట్** టూల్ ఫార్మాట్ ను ఉపయోగిస్తుంది — `name`, `description`, `parameters` టాప్-లెవెల్ కీలు (ఫంక్షన్ కింద కాదు).

**ముందు (చాట్ కంప్లీషన్స్ — సంక్లిష్ట):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**తర్వాత (స్పందనలు API — ఫ్లాట్):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

పూర్తిచేసిన ఉదాహరణ:
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
            "required": ["city_name"],       # అన్ని గుణాలు జాబితా చేయబడాలి
            "additionalProperties": False,   # కఠిన మోడ్ కోసం అవసరం
        },
    }
]
```

### టూల్ కాల్ రౌండ్-ట్రిప్ (అమలు చేసి ఫలితాలు తిరిగి ఇవ్వడం)

మోడల్ టూల్ కాల్ కోరినప్పుడు, `response.output` అంశాలు + `function_call_output` ఉపయోగించండి — **కాదు** చాట్ కంప్లీషన్స్ `role: assistant` + `role: tool` నమూనా.

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
    # మోడల్ యొక్క function_call అంశాలను సంభాషణకు జోడించండి
    messages.extend(response.output)

    # ప్రతి సాధనను అమలు చేసి ఫలితాలను జోడించండి
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # సాధన ఫలితాలతో తుది సమాధానాన్ని పొందండి
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### కొద్దిసార్లు టూల్ కాల్ ఉదాహరణలు

`input`లో టూల్ కాల్ కొద్దిసార్లు ఉదాహరణలు ఇస్తున్నప్పుడు `function_call` మరియు `function_call_output` అంశాలను ఉపయోగించండి. IDs `fc_` తో ప్రారంభమవ్వాలి.

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
# అంచనా వెబ్ శోధన ఉదాహరణ
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## చిత్రం ఇన్‌పుట్

చిత్రం కంటెంట్ అంశాలు `image_url` నుండి `input_image`గా మారుతుంది, మరియు URLnested object నుండి ఫ్లాట్ స్ట్రింగ్ గా మారుతుంది.

### చిత్రం ఇన్‌పుట్ — ముందు (చాట్ కంప్లీషన్స్)
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

### చిత్రం ఇన్‌పుట్ — తర్వాత (స్పందనలు API, URL)
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

### చిత్రం ఇన్‌పుట్ — తర్వాత (స్పందనలు API, base64)
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

> **ముఖ్య మార్పులు**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (నెస్టెడ్ ఆబ్జెక్ట్) → `"image_url": "..."` (ఫ్లాట్ స్ట్రింగ్ — HTTPS URL లేదా `data:image/...;base64,...` డేటా URI), (3) `"type": "text"` → `"type": "input_text"`.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ (MAF) మైగ్రేషన్

**మీ MAF వెర్షన్‌ను మొదట తనిఖీ చేయండి** — మైగ్రేషన్ MAF 1.0.0+ లేదా ప్రీ-1.0.0 బీటా/RC పై ఆధారపడి ఉంటుంది.

తనిఖీకి: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ లో, `OpenAIChatClient` **ఇప్పుడు ఇప్పటికే స్పందనలు API ను వాడుతుంది** — మార్పిడి అవసరం లేదు.

కోడ్‌బేస్ లెగసీ `OpenAIChatCompletionClient` (chat.completions.create ఉపయోగిస్తుంది) వాడితే, దాన్ని `OpenAIChatClient` తో మార్చండి:

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

### MAF ప్రీ-1.0.0 (బీటా/RC వర్షన్లు)

ప్రీ-1.0.0 MAF లో, `OpenAIChatClient` చాట్ కంప్లీషన్స్ ఉపయోగించింది. `agent-framework-openai>=1.0.0` కు అప్‌గ్రేడ్ చేయండి, అక్కడ `OpenAIChatClient` డిఫాల్ట్ గా స్పందనలు API ఉపయోగిస్తుంది.

> **గమనిక**: `Agent`, `MCPStreamableHTTPTool`, మరియు ఇతర MAF APIs మారలేదు — కేవలం క్లయింట్ క్లాస్ ఇంపోర్ట్ మరియు ప్రారంభం మారాయి.

## LangChain (`langchain-openai`) మైగ్రేషన్

`ChatOpenAI()` లో `use_responses_api=True` జోడించండి. అలాగే సందేశ కంటెంట్ యాక్సెస్‌ను `.content` నుండి `.text` గా మార్చండి.

ముందుగా:
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

# ... ఏజెంట్ ఆహ్వానం ...
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

> **ముఖ్య మార్పులు**: (1) కన్స్ట్రక్టర్ లో `use_responses_api=True`, (2) స్పందన సందేశాలలో `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->