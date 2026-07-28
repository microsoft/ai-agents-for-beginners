# Responses API चीट शीट (Python + Azure OpenAI)

> खालील सर्व कोड तुकडे मानून चालतात की `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` आहे आणि `client` आधीच इनिशियलाइज केलेले आहे (client सेटअप पहा).

## मूलभूत विनंती
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## क्लायंट सेटअप — EntraID (शिफारस केलेले)
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

## क्लायंट सेटअप — API की
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async क्लायंट सेटअप — EntraID
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

## Async क्लायंट सेटअप — स्पष्ट tenant सह EntraID (मल्टी-टेनंट)

जेव्हा Azure OpenAI स्रोत हा **विभिन्न tenant** मध्ये असेल तर `tenant_id` क्रेडेन्शियलमध्ये स्पष्टपणे द्या. हे सामान्यतः dev/test परिस्थितीत असते जिथे डेव्हलपरचा होम tenant स्रोताच्या tenant पेक्षा वेगळा असतो.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# उत्पादनासाठी ManagedIdentityCredential (Azure कंटेनर अॅप्स, अॅप सेवा, इत्यादी)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # वापरकर्त्याने नियुक्त केलेली व्यवस्थापित ओळख
)
# स्थानिक विकासासाठी AzureDeveloperCliCredential — स्पष्ट tenant_id आवश्यक आहे
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# साखळी: प्रथम व्यवस्थापित ओळख वापरून पहा, नंतर azd CLI कडे जा
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async क्लायंट स्थलांतरण — आधी/नंतर

आधी (डिप्रीकेटेड):
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

नंतर:
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

## संपूर्ण सिंक्रोनस स्थलांतरण — आधी/नंतर

आधी (लेगसी — Azure OpenAI Chat Completions):
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

नंतर (Responses API — Azure OpenAI v1 endpoint):
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

## स्ट्रीमिंग (सिंक)
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
        print()  # शेवटी नवीन ओळ
```

## स्ट्रीमिंग (असिंक)
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

## वेब अप स्ट्रीमिंग — बॅकएंड ते फ्रंटएंड स्वरूप

जेव्हा एखाद्या वेब अॅपचे स्थलांतरण करताना जे SSE/JSONL फ्रंटएंडकडे स्ट्रीम करते, तेव्हा **बॅकएंड सीरियलायझेशन फॉरमॅट** बदलते. नवीन बॅकएंड आउटपुट डिझाइन करा जे फ्रंटएंडच्या विद्यमान ऍक्सेस पॅटर्न्स जपेल जेणेकरून फ्रंटएंडमध्ये कोणताही बदल आवश्यक नाही.

**आधी** — Chat Completions बॅकएंड सहसा प्रत्येक चंकचा `choices[0]` dict सीरियलाइझ करतो:
```python
# जुना: प्रत्येक चंकसाठी सिरीयलाइझ केलेला संपूर्ण निवड शब्दकोश
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
फ्रंटएंड वाचतो: `response.delta.content` (चॉइस ऑब्जेक्ट मध्ये खोल).

**नंतर** — Responses API बॅकएंड एक लहान स्वरूप इमिट करतो जे फ्रंटएंड ऍक्सेस पथ जपतो:
```python
# नवीन: फक्त फ्रंटेंडला जे आवश्यक आहे तेच निघू द्या
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
फ्रंटएंड अजूनही `response.delta.content` वाचतो — **फ्रंटएंडमध्ये कोणताही बदल नाही**.

> **महत्त्वाचा मुद्दा**: Responses API स्ट्रीमिंग स्वरूप (`event.type` + `event.delta`) Chat Completions (`chunk.choices[0].delta.content`) पेक्षा मूलत: वेगळे आहे. पण तुमचा बॅकएंड ते फ्रंटएंड करार तुम्हाला ठरवायचा आहे. बॅकएंड आउटपुट असे डिझाइन करा जे फ्रंटएंड आधीच अपेक्षा करत आहे.

## स्ट्रीमिंग इव्हेंट क्रम

जेव्हा `stream: true` असेल, API खालील क्रमाने इव्हेंट्स पाठवते:
1. `response.created` – रिस्पॉन्स ऑब्जेक्ट इनिशियलाइज झाले
2. `response.in_progress` – जनरेशन सुरू झाले
3. `response.output_item.added` – आउटपुट आयटम तयार झाले
4. `response.content_part.added` – कंटेंट भाग सुरू झाला
5. `response.output_text.delta` – मजकूराचे भाग (अनेक, प्रत्येकात `delta: string` असते)
6. `response.output_text.done` – मजकूर जनरेशन पूर्ण
7. `response.content_part.done` – कंटेंट भाग पूर्ण
8. `response.output_item.done` – आउटपुट आयटम पूर्ण
9. `response.completed` – पूर्ण रिस्पॉन्स पूर्ण

फक्त मूलभूत मजकूर स्ट्रीमिंगसाठी, `response.output_text.delta` (मजकूर चंकसाठी) आणि `response.completed` (पूर्ण झाल्यावर) हाताळा.

## वेब अॅपमध्ये स्ट्रीमिंग त्रुटी हाताळणी

जेव्हा वेब अॅपमध्ये स्ट्रीम करताना, async iterator ला `try/except` मध्ये वेढा आणि त्रुटी JSON स्वरूपात पाठवा जेणेकरून फ्रंटएंड त्यांना सुसंगतपणे दाखवू शकते (उदा., दर मर्यादा, तात्पुरती अयशस्वीता):

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

> **हे का महत्वाचे आहे**: Azure OpenAI दर मर्यादा वेळेस `429 Too Many Requests` परत देते. `try/except` शिवाय स्ट्रीमिंग रिस्पॉन्स गुप्पटपणे संपते. त्यासह, फ्रंटएंडला `{"error": "Too Many Requests"}` मिळते आणि रिसेट_prompt दाखवू शकते.

## स्ट्रीमिंग इव्हेंट प्रकार (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## संभाषण स्वरूप
```python
# Responses API इनपुट अ‍ॅरेद्वारे संभाषण फॉरमॅटला समर्थन देते
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

## कंटेंट फिल्टर त्रुटी हाताळणी

त्रुटी बॉडीची रचना Chat Completions पासून Responses API पर्यंत बदलली आहे.

आधी (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

नंतर (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

महत्त्वाचे फरक:
- `innererror` wrapper **गेला** — कंटेंट फिल्टर तपशील आता `error.body` च्या शीर्ष स्तरावर आहे.
- `content_filter_result` (एकवचनी) → `content_filters` (बहुवचनी सूची) ज्यामध्ये प्रत्येक आयटममध्ये `content_filter_results` असतात.
- `content_filters` मधील प्रत्येक एन्ट्रीमध्ये `blocked`, `source_type`, आणि `content_filter_results` असतात ज्यात प्रत्येकी `jailbreak`, `hate`, `sexual`, `violence`, `self_harm` सारख्या श्रेणी तपशील असतात.

संपूर्ण Responses API कंटेंट फिल्टर त्रुटी बॉडी स्वरूप:
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

## रॉ HTTP स्थलांतरण (requests/httpx)

जर अॅप थेट Azure OpenAI REST कॉल करत असेल SDK वापरण्याऐवजी:

आधी (Chat Completions):
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

नंतर (Responses API):
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

> **टीप**: `output_text` हा Python SDK च्या `Response` ऑब्जेक्टवरील सोयीचा प्रॉपर्टी आहे. रॉ REST JSON रिस्पॉन्समध्ये टॉप-लेव्हल `output_text` फील्ड नाही — मजकूर `output[0].content[0].text` मध्ये असतो.

## मल्टी-टर्न संभाषण
```python
# प्रतिक्रियांस API वापरून संभाषण तयार करा
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# सहाय्यक प्रतिसाद संभाषणात जोडा
messages.append({"role": "assistant", "content": response.output_text})

# संभाषण सुरू ठेवा
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

कंटेंट प्रकार असलेले मल्टी-टर्न (स्पष्ट `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` द्वारे मल्टी-टर्न (पर्यायी)

स्वतः संभाषण अ‍ॅरे व्यवस्थापित करण्याऐवजी तुम्ही प्रतिक्रिया साखळी करू शकता
सर्व्हर-पक्षावर `previous_response_id` वापरून. API प्रत्येक रिस्पॉन्स साठवते आणि
स्वयंचलितपणे पूर्वीचे टर्न्स मूळे ठेवते.

```python
# पहिली वळण
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# पुढील वळणं — फक्त नवीन वापरकर्ता संदेश + मागील प्रतिसाद आयडी पाठवा
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**कधी कोणता वापरायचा:**

| पद्धत | फायदे | तोटे |
|---|---|---|
| `input` अ‍ॅरे (मॅन्युअल) | इतिहासावर पूर्ण नियंत्रण; ट्रिम/सारांश बनवू शकता; सर्व्हर-साइड स्टोरेज आवश्यक नाही (`store=False`) | जास्त कोड; तुम्ही अ‍ॅरे व्यवस्थापित करावा लागतो |
| `previous_response_id` | सोपा कोड; स्वयंचलित साखळी | `store=True` आवश्यक (डिफॉल्ट); संभाषण सर्व्हर-साइड साठवले जाते; कट्स दरम्यान इतिहास बदलता येत नाही |

> **स्थलांतरण टीप:** बहुतेक Chat Completions अ‍ॅप्स आधीच स्वतःची मेसेज अ‍ॅरे व्यवस्थापित करतात, त्यामुळे `input` अ‍ॅरे मध्ये रूपांतर थेट 1:1 स्थलांतरण आहे. नवीन कोडसाठी किंवा संभाषण इतिहासाला हात घालायची गरज नसल्यास `previous_response_id` वापरा.

## O-सिरीज.reasoning मॉडेल्स (o1, o3-mini, o3, o4-mini)

O-सिरीज मॉडेल्सना Responses API कडे स्थलांतरण करताना वेगळे पॅरामिटर बंधने आहेत.

### o-सिरीज साठी पॅरामिटर मॅपिंग

| Chat Completions (o-सिरीज) | Responses API | टीपा |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | जास्त सेट करा (4096+) — reasoning टोकन्स लिमिटमध्ये येतात |
| `reasoning_effort` | `reasoning.effort` | असल्यास तसा ठेवा (low/medium/high) |
| `temperature` | काढा किंवा `1` सेट करा | O-सिरीज फक्त `1` स्वीकारते |
| `top_p` | काढा | O-सिरीजवर सपोर्ट नाही |
| `seed` | काढा | Responses API मध्ये समर्थन नाही |

### O-सिरीज आधी/नंतर

आधी (Chat Completions सह o-सिरीज):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

नंतर (Responses API):
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

> **टीप**: O-सिरीज मॉडेल्स reasoning दरम्यान आउटपुट बफर करू शकतात आणि मजकूर डेल्टा पाठवण्यापूर्वी. स्ट्रीमिंग चालू राहतो पण प्रथम `response.output_text.delta` इव्हेंट GPT मॉडेल्सपेक्षा अधिक विलंबानंतर येऊ शकतो.

## reasoning टोकन्स ऍक्सेस करणे
```python
# तर्कशास्त्रीय मॉडेल्स अंतर्गत तर्कशक्ति वापरतात — तुम्ही किती तर्कशास्त्रीय टोकन्स वापरले गेले ते पाहू शकता
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

> **महत्त्वाचे**: reasoning मॉडेल्सच्या अंतर्गत reasoning प्रक्रियेसाठी `max_output_tokens=1000` वापरा (50-200 नव्हे). मॉडेल अंतर्गत reasoning टोकन्स वापरते नंतर अंतिम आउटपुट तयार करते.

## संरचित आउटपुट — JSON Schema
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

## टूल वापर

- `tools` मध्ये फंक्शन्स परिभाषित करा **flat Responses API फॉरमॅट** मध्ये — `name`, `description`, आणि `parameters` टॉप-लेव्हलवर (nested `function` अंतर्गत नाही).
- मॉडेल जेव्हा टूल कॉल करण्यास म्हणते तेव्हा तुमच्या अॅपमध्ये ते चालवा आणि नंतरच्या विनंतीत `function_call_output` आयटम म्हणून टूलचा निकाल `input` मध्ये जोडा.
- स्कीमास कमी ठेवा; कार्यान्वयन आधी इनपुट्स वैध करा.
- `strict: true` वापरताना सर्व प्रॉपर्टीज `required` मध्ये असाव्यात आणि `additionalProperties: false` अनिवार्य आहे.

> **⚠️ `pydantic_function_tool()` असंगत**: `openai.pydantic_function_tool()` पूर्वीचा Chat Completions nested फॉरमॅट तयार करतो (`{"type": "function", "function": {"name": ...}}`). ते `responses.create()` सोबत वापरू नका. टूल स्कीमा मॅन्युअली डिफाइन करा किंवा आउटपुट flatten करणारा wrapper लिहा.

### टूल डिफिनिशन फॉरमॅट

Responses API flat टूल फॉरमॅट वापरते — `name`, `description`, `parameters` टॉप-लेव्हल कीज आहेत (nested `function` अंतर्गत नाही).

**आधी (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**नंतर (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

पूर्ण उदाहरण:
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

`strict: true` सह (schema enforcement):
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
            "required": ["city_name"],       # सर्व मालमत्तांची यादी असणे आवश्यक आहे
            "additionalProperties": False,   # कडक मोडसाठी आवश्यक आहे
        },
    }
]
```

### टूल कॉल राउंड-ट्रिप (execute आणि निकाल परत करा)

जेव्हा मॉडेल टूल कॉलची विनंती करते, तेव्हा `response.output` आयटम + `function_call_output` वापरा — **Chat Completions मधील** `role: assistant` + `role: tool` पॅटर्न नाही.

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
    # मॉडेलचे function_call आयटम संभाषणात जोडा
    messages.extend(response.output)

    # प्रत्येक साधन चालवा आणि परिणाम जोडा
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # साधन परिणामांसह अंतिम प्रतिसाद मिळवा
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot टूल कॉल उदाहरणे

`input` मध्ये Few-shot टूल कॉल उदाहरणे प्रदान करताना `function_call` आणि `function_call_output` आयटम वापरा. IDs `fc_` ने सुरू होणे आवश्यक.

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
# अंगभूत वेब शोध उदाहरण
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## प्रतिमा इनपुट

प्रतिमा कंटेंट आयटमचे प्रकार `image_url` पासून `input_image` मध्ये बदलले गेले आहेत, आणि URL nested object पासून flat string मध्ये बदलला आहे.

### प्रतिमा इनपुट — आधी (Chat Completions)
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

### प्रतिमा इनपुट — नंतर (Responses API, URL)
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

### प्रतिमा इनपुट — नंतर (Responses API, base64)
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

> **मूलभूत बदल**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested object) → `"image_url": "..."` (flat string — HTTPS URL किंवा `data:image/...;base64,...` डेटा URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) स्थलांतरण

**सर्वप्रथम तुमची MAF आवृत्ती तपासा** — स्थलांतरण MAF 1.0.0+ किंवा प्री-1.0.0 beta/rc वर अवलंबून आहे.

तपासण्यासाठी: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ मध्ये, `OpenAIChatClient` **आधीच Responses API वापरतो** — स्थलांतरण आवश्यक नाही.

जर कोडबेस मध्ये जुन्या `OpenAIChatCompletionClient` (जो `chat.completions.create` वापरतो) वापरला जात असेल, तर तो `OpenAIChatClient` ने बदला:

आधी:
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

नंतर:
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

### MAF प्री-1.0.0 (beta/rc रिलीझेस)

प्री-1.0.0 MAF मध्ये, `OpenAIChatClient` Chat Completions वापरत होता. `agent-framework-openai>=1.0.0` मध्ये अपग्रेड करा जिथे `OpenAIChatClient` मूळतः Responses API वापरतो.

> **टीप**: `Agent`, `MCPStreamableHTTPTool`, आणि इतर MAF APIs मध्ये बदल नाही — फक्त क्लायंट क्लास इम्पोर्ट आणि निर्मिती बदलते.

## LangChain (`langchain-openai`) स्थलांतरण

`ChatOpenAI()` मध्ये `use_responses_api=True` जोडा. तसेच मेसेज कंटेंट ऍक्सेस `.content` वरून `.text` ला बदला.

आधी:
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

# ... एजंट आह्वान ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

नंतर:
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

# ... एजंट कॉल ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **महत्त्वाचे बदल**: (1) कन्स्ट्रक्टरमध्ये `use_responses_api=True`, (2) `.content` → `.text` प्रतिसाद संदेशांवर.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->