# प्रतिक्रियाहरू API चीट शीट (Python + Azure OpenAI)

> तलका सबै स्निपेटहरूले मान्छन् `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` र `client` पहिले नै इनिसियलाइज गरिएको छ (हेर्नुहोस् client सेटअप)।

## आधारभूत अनुरोध
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## क्लाइन्ट सेटअप — EntraID (सिफारिस गरिएको)
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

## क्लाइन्ट सेटअप — API कुंजी
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## असिंक्रोनस क्लाइन्ट सेटअप — EntraID
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

## असिंक्रोनस क्लाइन्ट सेटअप — स्पष्ट टेनेन्टसहित EntraID (बहु-टेनन्ट)

जब Azure OpenAI स्रोत **विभिन्न टेनेन्टमा** छ डिफल्ट भन्दा, क्रेडेन्शियलमा `tenant_id` स्पष्ट रूपमा पास गर्नुहोस्। यो सामान्यतया डिभ/टेस्ट परिदृश्यहरूमा हुन्छ जहाँ विकासकर्ताको गृह टेनेन्ट स्रोत टेनेन्टसँग फरक हुन्छ।

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# उत्पादनका लागि ManagedIdentityCredential (Azure Container Apps, App Service, आदि)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # प्रयोगकर्ता-निर्धारित प्रबन्धित पहिचान
)
# स्थानीय विकासका लागि AzureDeveloperCliCredential — स्पष्ट tenant_id अत्यावश्यक छ
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# श्रृंखला: पहिले प्रबन्धित पहिचान प्रयास गर्नुहोस्, पछि azd CLI उपयोग गर्नुहोस्
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## असिंक्रोनस क्लाइन्ट माइग्रेशन — पहिले/पछि

पहिले (डिप्रिकेट गरिएको):
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

पछि:
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

## पूर्ण सिन्क माइग्रेशन — पहिले/पछि

पहिले (पुरानो — Azure OpenAI Chat Completions):
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

पछि (प्रतिक्रियाहरू API — Azure OpenAI v1 अन्तःबिन्दु):
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

## स्ट्रिमिंग (सिन्क)
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
        print()  # अन्त्यमा नयाँ लाइन
```

## स्ट्रिमिंग (असिन्क)
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

## वेब एप स्ट्रिमिंग — ब्याकएन्डदेखि फ्रन्टएन्ड सम्मको रूप

SSE/JSONL स्ट्रिम गर्ने वेब एप माइग्रेट गर्दा, **ब्याकएन्ड सिरियलाइजेसन फार्म्याट** परिवर्तन हुन्छ। नयाँ ब्याकएन्ड आउटपुटलाई पुरानो फ्रन्टएन्ड पहुँच ढाँचासँग मिलाएर डिजाइन गर्नुहोस् ताकि फ्रन्टएन्डमा कुनै परिवर्तन आवश्यक नपरोस्।

**अघिल्लो** — Chat Completions ब्याकएन्डले सामान्यतया प्रत्येक चंक्सको `choices[0]` डिक्ट सिरियलाइज गर्थ्यो:
```python
# पुरानो: प्रति खण्ड श्रृंखलाबद्ध पूर्ण छनोट शब्दकोश
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
फ्रन्टएन्डले पढ्छ: `response.delta.content` (चयन वस्तुमा गहिराइमा)।

**पछिको** — प्रतिक्रियाहरू API ब्याकएन्डले कम्तिमा आकार निक्षेप गर्दछ जसले उही फ्रन्टएन्ड पहुँच पथ कायम राख्छ:
```python
# नयाँ: केवल फ्रन्टएन्डलाई चाहिने कुरा मात्र उत्सर्जन गर।
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
फ्रन्टएन्ड अझै पढ्छ `response.delta.content` — **फ्रन्टएन्डमा कुनै परिवर्तन आवश्यक छैन**।

> **मुख्य बुझाइ**: प्रतिक्रियाहरू API स्ट्रिमिंग आकार (`event.type` + `event.delta`) मौलिक रूपमा Chat Completions (`chunk.choices[0].delta.content`) भन्दा फरक छ। तर तपाईंको ब्याकएन्ड-देखि-फ्रन्टएन्ड सम्झौता तपाईंले नै परिभाषित गर्नुहुन्छ। ब्याकएन्ड आउटपुटलाई मिलाइदिनुहोस् जुन फ्रन्टएन्डले पहिले नै अपेक्षा गर्दछ।

## स्ट्रिमिंग घटना क्रम

जब `stream: true` हुन्छ, API यस क्रममा घटनाहरू पठाउँछ:
1. `response.created` – प्रतिक्रिया वस्तु आरम्भ
2. `response.in_progress` – उत्पादन सुरु भयो
3. `response.output_item.added` – आउटपुट वस्तु सिर्जना भयो
4. `response.content_part.added` – सामग्री भाग सुरु भयो
5. `response.output_text.delta` – पाठका टुक्राहरू (धेरै, प्रत्येकमा `delta: string` हुन्छ)
6. `response.output_text.done` – पाठ उत्पादन समाप्त
7. `response.content_part.done` – सामग्री भाग समाप्त
8. `response.output_item.done` – आउटपुट वस्तु समाप्त
9. `response.completed` – पूर्ण प्रतिक्रिया पूरा भयो

आधारभूत पाठ स्ट्रिमिंगका लागि, मात्र `response.output_text.delta` (पाठ टुक्राहरूका लागि) र `response.completed` (समाप्तिको लागि) ह्यान्डल गर्नुहोस्।

## वेब एपमा स्ट्रिमिंग त्रुटि ह्यान्डलिंग

वेब एपमा स्ट्रिमिंग गर्दा, असिंक्रोनस पुनरावृत्तिलाई `try/except` मा लपेट्नुहोस् र त्रुटिहरूलाई JSON स्वरूपमा यील्ड गर्नुहोस् ताकि फ्रन्टएन्डले तिनीहरूलाई सहजै प्रदर्शन गर्न सकोस् (जस्तै, रेट लिमिट, अस्थायी विफलताहरू):

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

> **किन यो महत्त्वपूर्ण छ**: Azure OpenAI ले रेट लिमिट हुँदा `429 Too Many Requests` फर्काउँछ। `try/except` बिना स्ट्रिमिंग प्रतिक्रिया नरमसँग बन्द हुन्छ। यसको साथ, फ्रन्टएन्डले `{"error": "Too Many Requests"}` प्राप्त गर्छ र पुन: प्रयास प्रॉम्प्ट देखाउन सक्छ।

## स्ट्रिमिंग घटना प्रकार (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## संवाद प्रारूप
```python
# Responses API ले इनपुट एर्रे मार्फत संवाद ढाँचालाई समर्थन गर्दछ
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

## सामग्री फिल्टर त्रुटि ह्यान्डलिंग

त्रुटि बडी संरचना Chat Completions बाट प्रतिक्रियाहरू API मा परिवर्तन भएको छ।

पहिले (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

पछि (प्रतिक्रियाहरू API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

मुख्य फरकहरू:
- `innererror` आवरण **गएको** — सामग्री फिल्टरको विवरण अब `error.body` को शीर्ष तहमा छ।
- `content_filter_result` (एकवचन) → `content_filters` (बहुवचन एरे) जसमा प्रत्येकमा `content_filter_results` (बहुवचन) हुन्छ।
- `content_filters` को प्रत्येक प्रविष्टिमा `blocked`, `source_type`, र `content_filter_results` हुन्छ जुन प्रत्येक वर्ग (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) को विवरण राख्छ।

पूर्ण प्रतिक्रियाहरू API सामग्री फिल्टर त्रुटि बडी आकार:
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

## कच्चा HTTP माइग्रेशन (requests/httpx)

यदि एपले Azure OpenAI REST सिधै कल गर्छ SDK प्रयोग नगरी:

पहिले (Chat Completions):
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

पछि (प्रतिक्रियाहरू API):
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

> **नोट**: `output_text` Python SDK को `Response` वस्तुमा सुविधा बस्तु हो। कच्चा REST JSON प्रतिक्रियामा शीर्ष तह `output_text` फिल्ड छैन — पाठ `output[0].content[0].text` मा हुन्छ।

## बहु-चरण संवाद
```python
# Responses API सँग संवाद सिर्जना गर्नुहोस्
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# सहायकको जवाफलाई संवादमा थप्नुहोस्
messages.append({"role": "assistant", "content": response.output_text})

# संवाद जारी राख्नुहोस्
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

सामग्री-प्रकारित बहु-चरण (स्पष्ट `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` द्वारा बहु-चरण (वैकल्पिक)

तपाईंले संवाद एरे आफैं व्यवस्थापन नगरी, सर्भर-पक्षमा `previous_response_id` प्रयोग गरी प्रतिक्रियाहरू श्रृंखला गर्न सक्नुहुन्छ। API प्रत्येक प्रतिक्रियालाई भण्डारण गर्छ र
पूर्वका चरणहरूलाई स्वचालित रूपमा अघि जोड्छ।


```python
# पहिलो पालो
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# पछि आउने पालाहरू — नयाँ प्रयोगकर्ताको सन्देश + अघिल्लो प्रतिक्रिया आईडी मात्र पास गर्नुहोस्
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**कहिले कुन प्रयोग गर्ने:**

| तरिका | फाइदाहरू | बेफाइदाहरू |
|---|---|---|
| `input` एरे (म्यानुअल) | इतिहासमाथि पूरै नियन्त्रण; ट्रिम/सारांश गर्न सकिन्छ; सर्भर-पक्ष भण्डारण आवश्यक छैन (`store=False`) | बढी कोड; तपाईं एरे आफैं व्यवस्थापन गर्नुहुन्छ |
| `previous_response_id` | सरल कोड; स्वचालित श्रृंखला | आवश्यक `store=True` (पूर्वनिर्धारित); संवाद सर्भर-पक्षमा भण्डारण; चरणहरूमाझ इतिहास परिवर्तन गर्न सकिन्न |

> **माइग्रेशन नोट:** धेरै Chat Completions एपहरूले पहिले नै आफ्नै सन्देश एरे व्यवस्थापन गर्छन्, त्यसैले `input` एरेमा रूपान्तरण सिधा १:१ माइग्रेशन हो। नयाँ कोड वा संवाद इतिहास परिवर्तन आवश्यक नहुनुमा `previous_response_id` प्रयोग गर्नुहोस्।

## O-श्रृंखला तर्क मोडेलहरू (o1, o3-mini, o3, o4-mini)

O-श्रृंखला मोडेलहरू प्रतिक्रियाहरू API मा माइग्रेट गर्दा विशेष प्यारामिटर सीमाहरू हुन्छन्।

### O-श्रृंखला प्यारामिटर म्यापिङ

| Chat Completions (o-श्रृंखला) | प्रतिक्रियाहरू API | टिप्पणीहरू |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | उच्च सेट गर्नुहोस् (4096+) — तर्क टोकनहरू सीमा भित्र गनिन्छन् |
| `reasoning_effort` | `reasoning.effort` | अस्तित्वमा भएअनुसार राख्नुहोस् (low/medium/high) |
| `temperature` | हटाउनुहोस् वा `1` मा सेट गर्नुहोस् | O-श्रृंखला केवल `1` स्वीकार्छ |
| `top_p` | हटाउनुहोस् | O-श्रृंखला मा समर्थन छैन |
| `seed` | हटाउनुहोस् | प्रतिक्रियाहरू API मा समर्थन छैन |

### O-श्रृंखला पहिले/पछि

पहिले (Chat Completions सहित o-श्रृंखला):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

पछि (प्रतिक्रियाहरू API):
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

> **नोट**: O-श्रृंखला मोडेलहरूले तर्क गर्दा आउटपुट बफर गर्न सक्छन् जुन पाठ डेल्टाहरू पठाउनु अघि। स्ट्रिमिंग अझै काम गर्छ तर पहिलो `response.output_text.delta` घटना GPT मोडेलहरू भन्दा लामो ढिलाइ पछी आउन सक्छ।

## तर्क टोकनहरू पहुँच
```python
# तर्क मोडेलहरूले आन्तरिक तर्क प्रयोग गर्छन् — तपाईंले कति तर्क टोकनहरू प्रयोग भए हेर्न सक्नुहुन्छ
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

> **महत्त्वपूर्ण**: तर्क मोडेलहरूको आन्तरिक तर्क प्रक्रियालाई ध्यानमा राखेर `max_output_tokens=1000` (५०–२०० होइन) प्रयोग गर्नुहोस्। मोडेलले अन्तिम आउटपुट सिर्जना अघि तर्क टोकनहरू भित्रै प्रयोग गर्छ।

## संरचित आउटपुट — JSON स्किमा
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

## उपकरण प्रयोग

- `tools` मा फङ्क्शनहरू परिभाषित गर्नुहोस् **फ्ल्याट प्रतिक्रियाहरू API फार्म्याट** मा — `name`, `description`, र `parameters` शीर्ष स्तरमा (न कि `function` अन्तर्गत नेस्ट गरिएको)।
- मोडेलले उपकरण कल गर्न भन्यो भने, तपाइँको एपमा कार्यान्वयन गर्नुहोस् र `function_call_output` वस्तुलाई `input` भित्र अर्को अनुरोधमा समावेश गर्नुहोस्।
- स्किमाहरूलाई न्यूनतम राख्नुहोस्; निष्पादन अघि इनपुटहरू प्रमाणित गर्नुहोस्।
- `strict: true` हुँदा, सबै गुणहरू `required` मा सूचीबद्ध हुनुपर्छ र `additionalProperties: false` अनिवार्य छ।

> **⚠️ `pydantic_function_tool()` असंगत छ**: `openai.pydantic_function_tool()` हेल्परले अझै पुरानै Chat Completions नेस्ट गरिएको फार्म्याट (`{"type": "function", "function": {"name": ...}}`) उत्पादन गर्छ। यसलाई `responses.create()` सँग प्रयोग नगर्नुहोस्। उपकरण स्किमाहरू म्यानुअली परिभाषित गर्नुहोस् वा आउटपुटलाई सपाट बनाउन र्यापर लेख्नुहोस्।

### उपकरण परिभाषा फार्म्याट

प्रतिक्रियाहरू API ले **फ्ल्याट** उपकरण फार्म्याट प्रयोग गर्छ — `name`, `description`, `parameters` शीर्ष स्तरका कुञ्जीहरू हुन् (न कि `function` अन्तर्गत नेस्ट गरिएको)।

**पहिले (Chat Completions — नेस्ट गरिएको):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**पछि (प्रतिक्रियाहरू API — फ्ल्याट):**
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

`strict: true` सँग (स्किमा कडाइ):
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
            "required": ["city_name"],       # सबै गुणहरू सूचीबद्ध हुनैपर्छ
            "additionalProperties": False,   # कडा मोडको लागि आवश्यक छ
        },
    }
]
```

### उपकरण कल राउन्ड-ट्रिप (निष्पादन र नतिजा फर्काउने)

मोडेलले उपकरण कल अनुरोध गर्दा, `response.output` वस्तुहरू + `function_call_output` प्रयोग गर्नुहोस् — **न कि** Chat Completions `role: assistant` + `role: tool` ढाँचा।

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
    # मोडेलको function_call वस्तुहरू कुरा चक्रमा थप्नुहोस्
    messages.extend(response.output)

    # प्रत्येक उपकरण चलाउनुहोस् र परिणामहरू थप्नुहोस्
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # उपकरण परिणामहरूसँग अन्तिम प्रतिक्रिया प्राप्त गर्नुहोस्
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### थोरै-शट उपकरण कल उदाहरणहरू

`input` मा उपकरण कलका थोरै-शट उदाहरणहरू प्रदान गर्दा, `function_call` र `function_call_output` वस्तुहरू प्रयोग गर्नुहोस्। आईडीहरू `fc_` बाट सुरु हुनुपर्छ।

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
# बिल्ट-इन वेब खोज उदाहरण
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## छवि इनपुट

छवि सामग्री वस्तुहरूको प्रकार `image_url` बाट `input_image` मा परिवर्तन हुन्छ, र URL नेस्ट गरिएको वस्तुबाट सपाट स्ट्रिङमा परिवर्तन हुन्छ।

### छवि इनपुट — पहिले (Chat Completions)
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

### छवि इनपुट — पछि (प्रतिक्रियाहरू API, URL)
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

### छवि इनपुट — पछि (प्रतिक्रियाहरू API, base64)
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

> **मुख्य परिवर्तनहरू**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (नेस्ट गरिएको वस्तु) → `"image_url": "..."` (सपाट स्ट्रिङ — HTTPS URL वा `data:image/...;base64,...` डेटा URI), (3) `"type": "text"` → `"type": "input_text"`.

## माइक्रोसफ्ट एजेन्ट फ्रेमवर्क (MAF) माइग्रेशन

**पहिले आफ्नो MAF संस्करण जाँच गर्नुहोस्** — माइग्रेशन MAF 1.0.0+ वा प्रि-1.0.0 बीटा/आरसीमा निर्भर हुन्छ।

जाँच गर्न: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ मा, `OpenAIChatClient` **पहिले नै प्रतिक्रियाहरू API प्रयोग गर्छ** — माइग्रेशन आवश्यक छैन।

यदि कोडबेसले पुरानो `OpenAIChatCompletionClient` (जसले `chat.completions.create` प्रयोग गर्छ) प्रयोग गर्छ भने, यसलाई `OpenAIChatClient` सँग बदल्नुहोस्:

पहिले:
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

पछि:
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

### MAF प्रि-1.0.0 (बीटा/आरसी रिलिजहरू)

प्रि-1.0.0 MAF मा, `OpenAIChatClient` ले Chat Completions प्रयोग गर्थ्यो। `agent-framework-openai>=1.0.0` मा अपग्रेड गर्नुहोस् जहाँ `OpenAIChatClient` डिफल्ट रूपमा प्रतिक्रियाहरू API प्रयोग गर्दछ।

> **नोट**: `Agent`, `MCPStreamableHTTPTool`, र अन्य MAF API हरू अपरिवर्तित रहन्छन् — केवल क्लाइन्ट क्लास इम्पोर्ट र इनिसिएसन परिवर्तन हुन्छ।

## LangChain (`langchain-openai`) माइग्रेशन

`ChatOpenAI()` मा `use_responses_api=True` थप्नुहोस्। साथै सन्देश सामग्री पहुँच `.content` बाट `.text` मा अपडेट गर्नुहोस्।

पहिले:
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

# ... एजेन्ट आवाहन ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

पछि:
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

# ... एजेन्ट कल ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **मुख्य परिवर्तनहरू**: (1) कन्स्ट्रक्टरमा `use_responses_api=True`, (2) प्रतिक्रिया सन्देशहरूमा `.content` → `.text`।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->