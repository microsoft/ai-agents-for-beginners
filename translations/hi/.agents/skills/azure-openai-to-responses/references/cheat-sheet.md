# Responses API चीट शीट (Python + Azure OpenAI)

> नीचे दिए गए सभी स्निपेट यह मानते हैं कि `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` और `client` पहले से इनिशियलाइज़्ड है (देखें client सेटअप)।

## मूल अनुरोध
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## क्लाइंट सेटअप — EntraID (सिफारिश की गई)
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

## क्लाइंट सेटअप — API कुंजी
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async क्लाइंट सेटअप — EntraID
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

## Async क्लाइंट सेटअप — स्पष्ट टेनेंट के साथ EntraID (मल्टी-टेनेंट)

जब Azure OpenAI संसाधन **डिफ़ॉल्ट से अलग टेनेंट** में हो, तो क्रेडेंशियल में `tenant_id` स्पष्ट रूप से पास करें। यह सामान्यतः dev/test परिदृश्यों में होता है जहां डेवलपर का होम टेनेंट संसाधन टेनेंट से अलग होता है।

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# उत्पादन के लिए ManagedIdentityCredential (Azure Container Apps, App Service, आदि)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # उपयोगकर्ता आवंटित प्रबंधित पहचान
)
# स्थानीय विकास के लिए AzureDeveloperCliCredential — स्पष्ट tenant_id महत्वपूर्ण है
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# श्रृंखला: पहले प्रबंधित पहचान का प्रयास करें, फिर azd CLI पर वापस जाएं
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async क्लाइंट माइग्रेशन — पहले/बाद में

पहले (पुराना):
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

बाद में:
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

## पूर्ण सिंक माइग्रेशन — पहले/बाद में

पहले (पुराना — Azure OpenAI चैट पूर्णताएं):
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

बाद में (Responses API — Azure OpenAI v1 Endpoint):
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
        print()  # अंत में नया लाइन
```

## स्ट्रीमिंग (Async)
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

## वेब ऐप स्ट्रीमिंग — Backend से Frontend आकृति

जब किसी वेब ऐप को माइग्रेट करते हैं जो SSE/JSONL स्ट्रीम करता है फ्रंटेंड को, तो **बैकेंड सीरियलाइज़ेशन फॉर्मेट** बदल जाता है। नए बैकेंड आउटपुट को ऐसा डिजाइन करें कि फ्रंटेंड की मौजूदा एक्सेस पैटर्न संरक्षित रहें ताकि फ्रंटेंड में कोई बदलाव न करना पड़े।

**पहले** — चैट पूर्णताएं बैकेंड आमतौर पर प्रत्येक चंक का `choices[0]` dict सीरियलाइज़ करता था:
```python
# पुराना: प्रत्येक चंक के लिए अनुक्रमित पूर्ण विकल्प शब्दकोश
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
फ्रंटेंड पढ़ता है: `response.delta.content` (choice ऑब्जेक्ट के भीतर गहरा पथ)।

**बाद में** — Responses API बैकेंड न्यूनतम आकृति देता है जो समान फ्रंटेंड एक्सेस पथ संरक्षित करता है:
```python
# नया: केवल वही भेजें जो फ्रंटेंड को चाहिए
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
फ्रंटेंड अभी भी पढ़ता है `response.delta.content` — **फ्रंटेंड में कोई बदलाव आवश्यक नहीं**।

> **मुख्य समझ**: Responses API स्ट्रीमिंग आकृति (`event.type` + `event.delta`) मूलतः अलग है चैट पूर्णताओं से (`chunk.choices[0].delta.content`)। लेकिन आपका बैकेंड-से-फ्रंटेंड अनुबंध आपका अपना होता है। बैकेंड आउटपुट को फ्रंटेंड की वर्तमान अपेक्षा के अनुसार आकार दें।

## स्ट्रीमिंग इवेंट अनुक्रम

जब `stream: true` हो, API इस क्रम में इवेंट भेजती है:
1. `response.created` – प्रतिक्रिया ऑब्जेक्ट इनिशियलाइज़्ड
2. `response.in_progress` – सृजन शुरू हुआ
3. `response.output_item.added` – आउटपुट आइटम बनाया गया
4. `response.content_part.added` – कंटेंट हिस्सा शुरू हुआ
5. `response.output_text.delta` – टेक्स्ट चंक्स (कई, प्रत्येक में `delta: string` होता है)
6. `response.output_text.done` – टेक्स्ट निर्माण समाप्त हुआ
7. `response.content_part.done` – कंटेंट हिस्सा समाप्त हुआ
8. `response.output_item.done` – आउटपुट आइटम समाप्त हुआ
9. `response.completed` – पूर्ण प्रतिक्रिया पूरी हुई

मूल टेक्स्ट स्ट्रीमिंग के लिए, केवल `response.output_text.delta` (टेक्स्ट चंक्स के लिए) और `response.completed` (समाप्ति के लिए) को संभालें।

## वेब ऐप्स में स्ट्रीमिंग त्रुटि हैंडलिंग

वेब ऐप में स्ट्रीमिंग करते समय, async iteration को `try/except` में लपेटें और त्रुटियों को JSON के रूप में वापस दें ताकि फ्रंटेंड उन्हें सुंदरता से प्रदर्शित कर सके (जैसे, रेट लिमिट्स, अस्थायी विफलताएं):

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

> **क्यों यह महत्वपूर्ण है**: Azure OpenAI रेट लिमिटिंग के दौरान `429 Too Many Requests` लौटाता है। `try/except` के बिना, स्ट्रीमिंग प्रतिक्रिया चुपचाप बंद हो जाती है। इसके साथ, फ्रंटेंड को `{"error": "Too Many Requests"}` मिलता है और वह पुनः प्रयास प्रॉम्प्ट दिखा सकता है।

## स्ट्रीमिंग इवेंट प्रकार (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## वार्तालाप प्रारूप
```python
# Responses API इनपुट एरे के माध्यम से बातचीत प्रारूप का समर्थन करता है
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

## कंटेंट फ़िल्टर त्रुटि हैंडलिंग

त्रुटि बॉडी संरचना Chat Completions से Responses API में बदल गई है।

पहले (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

बाद में (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

मुख्य अंतर:
- `innererror` आवरण **हटा दिया गया है** — कंटेंट फ़िल्टर विवरण अब `error.body` के शीर्ष स्तर पर हैं।
- `content_filter_result` (एकवचन) → `content_filters` (बहुवचन सरणी) जिसमें प्रत्येक प्रविष्टि के भीतर `content_filter_results` (बहुवचन) शामिल हैं।
- `content_filters` की प्रत्येक प्रविष्टि में `blocked`, `source_type`, और `content_filter_results` होती है जिसमें प्रति-श्रेणी विवरण होते हैं (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`)।

Responses API कंटेंट फ़िल्टर त्रुटि बॉडी की पूर्ण आकृति:
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

## Raw HTTP माइग्रेशन (requests/httpx)

यदि ऐप सीधे Azure OpenAI REST कॉल करता है बजाय SDK का उपयोग करने के:

पहले (Chat Completions):
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

बाद में (Responses API):
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

> **नोट**: `output_text` Python SDK के `Response` ऑब्जेक्ट पर एक सुविधा संपत्ति है। कच्ची REST JSON प्रतिक्रिया में शीर्ष स्तर पर `output_text` फ़ील्ड नहीं होती — टेक्स्ट `output[0].content[0].text` पर होता है।

## बहु-टर्न बातचीत
```python
# प्रतिक्रियाओं API के साथ एक बातचीत बनाएं
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# सहायक की प्रतिक्रिया वार्तालाप में जोड़ें
messages.append({"role": "assistant", "content": response.output_text})

# बातचीत जारी रखें
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

कंटेंट-प्रकारित बहु-टर्न (स्पष्ट `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` के माध्यम से बहु-टर्न (वैकल्पिक)

अपने आप वार्तालाप सूची प्रबंधित करने के बजाय, आप सर्वर-साइड `previous_response_id` के साथ प्रतिक्रिया चेन कर सकते हैं।
API प्रत्येक प्रतिक्रिया को संग्रहीत करता है और
स्वचालित रूप से पिछली पारियां पहले से जोड़ता है।

```python
# पहला मोड़
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# बाद के मोड़ — केवल नया उपयोगकर्ता संदेश + पिछले प्रतिक्रिया ID पास करें
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**कहां कौन सा उपयोग करें:**

| तरीका | फायदे | नुकसान |
|---|---|---|
| `input` सूची (मैनुअल) | इतिहास पर पूर्ण नियंत्रण; ट्रिम/सारांश कर सकते हैं; सर्वर-साइड स्टोरेज की आवश्यकता नहीं (`store=False`) | अधिक कोड; सूची आप ही प्रबंधित करते हैं |
| `previous_response_id` | सरल कोड; स्वचालित चेनिंग | `store=True` (डिफ़ॉल्ट) आवश्यक; बातचीत सर्वर-साइड संग्रहीत; टर्न्स के बीच इतिहास संशोधित नहीं कर सकते |

> **माइग्रेशन नोट:** अधिकांश Chat Completions ऐप्स पहले से अपनी संदेश सूची प्रबंधित करते हैं, इसलिए `input` सूची में परिवर्तन अधिक सीधे 1:1 माइग्रेशन जैसा है। नया कोड या जब बातचीत इतिहास को संशोधित नहीं करना हो तब `previous_response_id` का उपयोग करें।

## O-सीरीज तर्क मॉडल (o1, o3-mini, o3, o4-mini)

O-सीरीज मॉडल Responses API पर माइग्रेट करते समय अद्वितीय पैरामीटर प्रतिबंध रखते हैं।

### o-सीरीज के लिए पैरामीटर मैपिंग

| Chat Completions (o-सीरीज) | Responses API | नोट्स |
|---|---|---|

| `max_completion_tokens` | `max_output_tokens` | उच्च सेट करें (4096+) — तर्क टोकन सीमा के खिलाफ गिनते हैं |
| `reasoning_effort` | `reasoning.effort` | यदि मौजूद हो तो यथावत रखें (कम/मध्यम/उच्च) |
| `temperature` | हटा दें या `1` सेट करें | O-सीरीज़ केवल `1` स्वीकार करती है |
| `top_p` | हटा दें | o-सीरीज़ पर समर्थित नहीं है |
| `seed` | हटा दें | Responses API में समर्थित नहीं है |

### O-सीरीज़ पहले/बाद में

पहले (o-सीरीज़ के साथ चैट पूर्णताएँ):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

बाद में (Responses API):
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

> **नोट**: O-सीरीज़ मॉडल तर्क के दौरान आउटपुट को बफ़र कर सकते हैं इससे पहले कि वे टेक्स्ट डेल्टा को जारी करें। स्ट्रीमिंग अभी भी काम करता है लेकिन पहला `response.output_text.delta` ईवेंट GPT मॉडल की तुलना में अधिक विलंब के बाद आ सकता है।

## तर्क टोकन तक पहुँच
```python
# तर्क मॉडल आंतरिक तर्क का उपयोग करते हैं — आप देख सकते हैं कि कितने तर्क टोकन का उपयोग किया गया था
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

> **महत्वपूर्ण**: अंतर्निहित तर्क प्रक्रिया के लिए reasoning मॉडल के लिए `max_output_tokens=1000` (50–200 नहीं) का उपयोग करें। मॉडल अंतिम आउटपुट उत्पन्न करने से पहले आंतरिक रूप से तर्क टोकन का उपयोग करता है।

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

## उपकरण उपयोग

- `tools` में फ़ंक्शंस को परिभाषित करें **फ्लैट Responses API फ़ॉर्मेट** के साथ — शीर्ष स्तर पर `name`, `description`, और `parameters` (न कि `function` के अंतर्गत नेस्टेड)।
- जब मॉडल किसी टूल को कॉल करने के लिए कहता है, तो इसे अपने ऐप में निष्पादित करें और अगले अनुरोध में टूल परिणाम को `function_call_output` आइटम के रूप में `input` के भीतर शामिल करें।
- स्कीमाओं को न्यूनतम रखें; निष्पादन से पहले इनपुट मान्य करें।
- जब `strict: true` का उपयोग किया जाए, तो सभी गुण `required` में सूचीबद्ध होने चाहिए और `additionalProperties: false` अनिवार्य है।

> **⚠️ `pydantic_function_tool()` असंगत है**: `openai.pydantic_function_tool()` सहायक अभी भी पुराने Chat Completions नेस्टेड फ़ॉर्मेट (`{"type": "function", "function": {"name": ...}}`) का उत्पादन करता है। इसे `responses.create()` के साथ उपयोग न करें। टूल स्कीमाओं को मैन्युअल रूप से परिभाषित करें या आउटपुट को फ्लैट करने के लिए रैपर लिखें।

### टूल परिभाषा प्रारूप

Responses API **फ्लैट** टूल प्रारूप का उपयोग करता है — `name`, `description`, और `parameters` शीर्ष-स्तर कीज़ हैं (न कि `function` के अंतर्गत नेस्टेड)।

**पहले (Chat Completions — नेस्टेड):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**बाद में (Responses API — फ्लैट):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

पूरा उदाहरण:
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

`strict: true` के साथ (स्कीमा प्रवर्तन):
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
            "required": ["city_name"],       # सभी गुणों को सूचीबद्ध किया जाना चाहिए
            "additionalProperties": False,   # सख्त मोड के लिए आवश्यक
        },
    }
]
```

### टूल कॉल राउंड-ट्रिप (निष्पादित करें और परिणाम लौटाएँ)

जब मॉडल टूल कॉल का अनुरोध करता है, तो `response.output` आइटम + `function_call_output` का उपयोग करें — **न कि** Chat Completions का `role: assistant` + `role: tool` पैटर्न।

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
    # मॉडल के function_call आइटम्स को बातचीत में जोड़ें
    messages.extend(response.output)

    # प्रत्येक टूल को चलाएं और परिणाम जोड़ें
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # टूल परिणामों के साथ अंतिम प्रतिक्रिया प्राप्त करें
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### कुछ-शॉट टूल कॉल उदाहरण

`input` में टूल कॉल के कुछ-शॉट उदाहरण प्रदान करते समय, `function_call` और `function_call_output` आइटम का उपयोग करें। IDs को `fc_` से शुरू होना चाहिए।

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

छवि सामग्री आइटम का प्रकार `image_url` से `input_image` में बदल गया है, और URL एक नेस्टेड ऑब्जेक्ट से एक फ्लैट स्ट्रिंग में बदल गया है।

### छवि इनपुट — पहले (Chat Completions)
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

### छवि इनपुट — बाद में (Responses API, URL)
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

### छवि इनपुट — बाद में (Responses API, base64)
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

> **मुख्य परिवर्तन**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (नेस्टेड ऑब्जेक्ट) → `"image_url": "..."` (फ्लैट स्ट्रिंग — या तो HTTPS URL या `data:image/...;base64,...` डेटा URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft एजेंट फ्रेमवर्क (MAF) माइग्रेशन

**सबसे पहले अपना MAF संस्करण जांचें** — माइग्रेशन इस बात पर निर्भर करता है कि आप MAF 1.0.0+ पर हैं या पूर्व-1.0.0 बीटा/आरसी पर।

जांचने के लिए: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+ में, `OpenAIChatClient` **पहले से Responses API का उपयोग करता है** — किसी माइग्रेशन की आवश्यकता नहीं।

यदि कोडबेस पुराने `OpenAIChatCompletionClient` (जो `chat.completions.create` का उपयोग करता है) का उपयोग करता है, तो इसे `OpenAIChatClient` से बदलें:

पहले:
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

बाद में:
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

### MAF पूर्व-1.0.0 (बीटा/आरसी रिलीज़)

पूर्व-1.0.0 MAF में, `OpenAIChatClient` ने Chat Completions का उपयोग किया। `agent-framework-openai>=1.0.0` में अपग्रेड करें जहां `OpenAIChatClient` डिफ़ॉल्ट रूप से Responses API का उपयोग करता है।

> **नोट**: `Agent`, `MCPStreamableHTTPTool`, और अन्य MAF API अपरिवर्तित रहते हैं — केवल क्लाइंट क्लास आयात और उदाहरण बदलता है।

## LangChain (`langchain-openai`) माइग्रेशन

`ChatOpenAI()` में `use_responses_api=True` जोड़ें। साथ ही संदेश सामग्री पहुँच `.content` से `.text` में अपडेट करें।

पहले:
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

# ... एजेंट आह्वान ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

बाद में:
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

# ... एजेंट आह्वान ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **मुख्य परिवर्तन**: (1) कंस्ट्रक्टर में `use_responses_api=True`, (2) प्रतिक्रिया संदेशों पर `.content` → `.text`।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->