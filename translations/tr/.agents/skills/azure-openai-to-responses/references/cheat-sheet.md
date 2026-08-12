# Yanıtlar API Hızlı Referans Tablosu (Python + Azure OpenAI)

> Aşağıdaki tüm örnekler `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` varsaymakta ve `client` zaten başlatılmıştır (bkz. istemci kurulumu).

## Temel istek
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## İstemci kurulumu — EntraID (önerilen)
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

## İstemci kurulumu — API anahtarı
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Asenkron istemci kurulumu — EntraID
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

## Açık kiracı ile asenkron istemci kurulumu — EntraID (çok kiracılı)

Azure OpenAI kaynağı varsayılandan **farklı bir kiracıdayken**, `tenant_id` kimlik bilgilerine açıkça geçilmelidir. Bu, geliştirici ev kiracısı kaynak kiracısından farklı olduğu geliştirici/test senaryolarında yaygındır.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# Üretim için ManagedIdentityCredential (Azure Container Apps, App Service, vb.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # kullanıcıya atanmış yönetilen kimlik
)
# Yerel geliştirme için AzureDeveloperCliCredential — açıkça belirtilmiş tenant_id kritik önemdedir
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Zincir: önce yönetilen kimliği dene, başarısız olursa azd CLI'ya geçiş yap
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Asenkron istemci göçü — önce/sonra

Önce (kullanımdan kaldırıldı):
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

Sonra:
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

## Tam senkron göç — önce/sonra

Önce (eski — Azure OpenAI Sohbet Tamamlamaları):
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

Sonra (Yanıtlar API — Azure OpenAI v1 uç noktası):
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

## Akış (senkron)
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
        print()  # satır sonunda yeni satır
```

## Akış (asenkron)
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

## Web uygulaması akışı — arka uçtan ön uca yapı

SSE/JSONL akışını ön uca gönderen bir web uygulaması taşınırken, **arka uç serileştirme formatı** değişir. Yeni arka uç çıktısını, ön ucun mevcut erişim desenlerini koruyacak şekilde tasarlayın; böylece ön uçta değişiklik gerekmez.

**Önce** — Sohbet Tamamlamaları arka ucu genellikle her parçanın `choices[0]` sözlüğünü serileştirirdi:
```python
# Eski: parça başına serileştirilmiş tam seçim sözlüğü
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Ön uç okuma: `response.delta.content` (choice nesnesinde derin bir yol).

**Sonra** — Yanıtlar API arka ucu aynı ön uç erişim yolunu korunacak minimal bir yapı yayınlar:
```python
# Yeni: sadece ön yüzün ihtiyacı olanı yayınla
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Ön uç hala `response.delta.content` okur — **ön uçta değişiklik gerekmez**.

> **Ana çıkarım**: Yanıtlar API akış yapısı (`event.type` + `event.delta`) Sohbet Tamamlamaları (`chunk.choices[0].delta.content`) temelinden farklıdır. Ancak arka uçtan ön uca sözleşmeniz size aittir. Arka uç çıktısını, ön ucun zaten beklediği şekilde şekillendirin.

## Akış olay dizisi

`stream: true` olduğunda API bu sırayla olaylar gönderir:
1. `response.created` – yanıt nesnesi başlatıldı
2. `response.in_progress` – üretim başladı
3. `response.output_item.added` – çıktı öğesi oluşturuldu
4. `response.content_part.added` – içerik parçası başladı
5. `response.output_text.delta` – metin parçacıkları (birden çok, her biri `delta: string` içerir)
6. `response.output_text.done` – metin üretimi tamamlandı
7. `response.content_part.done` – içerik parçası tamamlandı
8. `response.output_item.done` – çıktı öğesi tamamlandı
9. `response.completed` – tam yanıt tamamlandı

Temel metin akışı için, sadece `response.output_text.delta` (metin parçaları için) ve `response.completed` (tamamlama için) ele alınmalıdır.

## Web uygulamalarında akış hata yönetimi

Akış yaparken, asenkron yinelemeyi `try/except` içine alın ve hataları JSON olarak iletin, böylece ön uç sakin bir şekilde gösterebilir (örneğin, hız limiti, geçici hatalar):

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

> **Neden önemli**: Azure OpenAI hız limitlerinde `429 Too Many Requests` döner. `try/except` olmadan, akış yanıtı sessizce sonlanır. `try/except` ile ön uç `{"error": "Too Many Requests"}` alır ve tekrar deneme uyarısı gösterebilir.

## Akış olay türleri (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Konuşma formatı
```python
# Responses API, giriş dizisi aracılığıyla sohbet formatını destekler
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

## İçerik filtresi hata yönetimi

Hata gövdesi yapısı Chat Tamamlamalarından Yanıtlar API'ye değişti.

Önce (Chat Tamamlamalar):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Sonra (Yanıtlar API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Temel farklar:
- `innererror` sarmalayıcısı **kaldırıldı** — içerik filtresi detayları artık `error.body` üst seviyesinde.
- `content_filter_result` (tekil) → `content_filters` (çoğul dizi) ve her girdi içinde `content_filter_results` (çoğul).
- `content_filters` içindeki her girdi `blocked`, `source_type` ve kategoriye göre ayrıntılar (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`) içeren `content_filter_results` içerir.

Yanıtlar API içerik filtresi hata gövdesi tam şekli:
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

## Ham HTTP geçişi (requests/httpx)

Uygulama SDK yerine doğrudan Azure OpenAI REST çağırıyorsa:

Önce (Chat Tamamlamalar):
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

Sonra (Yanıtlar API):
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

> **Not**: `output_text`, Python SDK'sındaki `Response` nesnesinin kolaylık özelliğidir. Ham REST JSON yanıtı üst seviyede `output_text` alanı barındırmaz — metin `output[0].content[0].text` konumundadır.

## Çok aşamalı konuşma
```python
# Yanıtlar API'si ile bir konuşma oluşturun
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Asistanın yanıtını konuşmaya ekle
messages.append({"role": "assistant", "content": response.output_text})

# Konuşmaya devam et
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Türlendirilmiş çok aşamalı (açık `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` ile çok aşamalı (alternatif)

Konuşma dizisini kendiniz yönetmek yerine, yanıtları
sunucu tarafında `previous_response_id` kullanarak zincirleyebilirsiniz. API her yanıtı saklar ve
önceki dönüşleri otomatik olarak başa ekler.

```python
# İlk tur
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Sonraki turlar — sadece yeni kullanıcı mesajını + önceki yanıt kimliğini geçirin
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Ne zaman hangisi kullanılır:**

| Yöntem | Artıları | Eksileri |
|---|---|---|
| `input` dizisi (manuel) | Geçmiş üzerinde tam kontrol; kırpma/özetleme yapılabilir; sunucu tarafı depolama gerekmez (`store=False`) | Daha fazla kod; diziyi siz yönetirsiniz |
| `previous_response_id` | Daha basit kod; otomatik zincirleme | `store=True` (varsayılan) olmalı; konuşma sunucu tarafında saklanır; dönüşler arasında geçmiş düzenlenemez |

> **Geçiş notu:** Çoğu Sohbet Tamamlamaları uygulaması kendi mesaj dizisini zaten yönetir, bu nedenle `input` dizisine geçiş daha doğrudan 1'e 1 dönüşümdür. Yeni kod veya geçmiş manipülasyonu gerekmediğinde `previous_response_id` kullanın.

## O-serisi akıl yürütme modelleri (o1, o3-mini, o3, o4-mini)

O-serisi modeller, Yanıtlar API'ye geçerken benzersiz parametre kısıtlamalarına sahiptir.

### O-serisi parametre eşlemesi

| Sohbet Tamamlamaları (o-serisi) | Yanıtlar API | Notlar |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Yüksek ayarlayın (4096+) — akıl yürütme tokenları limite sayılır |
| `reasoning_effort` | `reasoning.effort` | Mevcutsa olduğu gibi bırakın (düşük/orta/yüksek) |
| `temperature` | Kaldırın veya `1` yapın | O-serisi sadece `1` kabul eder |
| `top_p` | Kaldırın | O-serisinde desteklenmez |
| `seed` | Kaldırın | Yanıtlar API'de desteklenmez |

### O-serisi önce/sonra

Önce (O-serisi ile Sohbet Tamamlamaları):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Sonra (Yanıtlar API):
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

> **Not**: O-serisi modeller, akıl yürütürken metin delta yayınlamadan önce çıktı tamponlayabilir. Akış yine de çalışır, ancak ilk `response.output_text.delta` olayı GPT modellerindekinden daha uzun gecikmeyle gelebilir.

## Akıl yürütme tokenlarına erişim
```python
# Akıl yürütme modelleri dahili akıl yürütmeyi kullanır — kaç tane akıl yürütme belirteci kullanıldığını görebilirsiniz
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

> **Önemli**: Akıl yürütme modellerinin içsel sürecini hesaba katmak için `max_output_tokens=1000` kullanın (50–200 değil). Model, son çıktıyı üretmeden önce dahili olarak akıl yürütme tokenları kullanır.

## Yapılandırılmış çıktı — JSON Şeması
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

## Araç kullanımı

- `tools` içinde fonksiyonları **düz Yanıtlar API formatı** ile tanımlayın — `name`, `description` ve `parameters` üst seviyede olmalı (fonksiyon altında iç içe değil).
- Model araç çağrısı istediğinde, uygulamanızda çalıştırın ve sonuçları sonraki istekte `input` içinde `function_call_output` öğesi olarak dahil edin.
- Şemaları minimal tutun; yürütmeden önce girdileri doğrulayın.
- `strict: true` kullanılırken, tüm özellikler `required` içinde listelenmeli ve `additionalProperties: false` zorunludur.

> **⚠️ `pydantic_function_tool()` uyumsuzdur**: `openai.pydantic_function_tool()` yardımcı fonksiyonu hâlâ eski Sohbet Tamamlamaları iç içe formatını (`{"type": "function", "function": {"name": ...}}`) üretir. Bunu `responses.create()` ile kullanmayın. Araç şemalarını manuel tanımlayın ya da çıktıyı düzleştirmek için bir sarıcı yazın.

### Araç tanım formatı

Yanıtlar API **düz** bir araç formatı kullanır — `name`, `description`, `parameters` üst seviyede anahtarlardır (fonksiyonun altında değil).

**Önce (Sohbet Tamamlamaları — iç içe):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Sonra (Yanıtlar API — düz):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Tam örnek:
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

`strict: true` ile (şema uygulanması):
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
            "required": ["city_name"],       # Tüm özellikler listelenMELİDİR
            "additionalProperties": False,   # Katı mod için gereklidir
        },
    }
]
```

### Araç çağrısı tam turu (çalıştır ve sonuçları geri döndür)

Model araç çağrısı istediğinde, `response.output` öğeleri + `function_call_output` kullanın — Sohbet Tamamlamaları `role: assistant` + `role: tool` kalıbı **kullanmayın**.

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
    # Modelin function_call öğelerini sohbete ekle
    messages.extend(response.output)

    # Her aracı çalıştır ve sonuçları ekle
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Araç sonuçlarıyla nihai yanıtı al
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Az örnekli araç çağrısı örnekleri

`input` içinde az örnekli araç çağrı örnekleri verirken `function_call` ve `function_call_output` öğelerini kullanın. Kimlikler `fc_` ile başlamalıdır.

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
# Yerleşik web arama örneği
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Görsel girişi

Görsel içerik öğelerinin türü `image_url`'den `input_image`'e değişir ve URL iç içe nesneden düz bir stringe dönüşür.

### Görsel girişi — önce (Sohbet Tamamlamaları)
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

### Görsel girişi — sonra (Yanıtlar API, URL)
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

### Görsel girişi — sonra (Yanıtlar API, base64)
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

> **Ana değişiklikler**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (iç içe nesne) → `"image_url": "..."` (düz string — HTTPS URL veya `data:image/...;base64,...` veri URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) geçişi

**Önce MAF sürümünüzü kontrol edin** — geçiş, MAF 1.0.0+ mu yoksa 1.0.0 öncesi beta/rc mi olduğuna bağlıdır.

Kontrol etmek için: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+'da `OpenAIChatClient` **zaten Yanıtlar API'yi kullanıyor** — geçiş gerekmez.

Kod tabanı eski `OpenAIChatCompletionClient` (ki bu `chat.completions.create` kullanır) kullanıyorsa, `OpenAIChatClient` ile değiştirin:

Önce:
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

Sonra:
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

### MAF 1.0.0 öncesi (beta/rc sürümleri)

1.0.0 öncesi MAF'da `OpenAIChatClient` Sohbet Tamamlamaları kullanıyordu. `agent-framework-openai>=1.0.0`'ye geçin; burada `OpenAIChatClient` varsayılan olarak Yanıtlar API'yi kullanır.

> **Not**: `Agent`, `MCPStreamableHTTPTool` ve diğer MAF API'leri değişmez — sadece istemci sınıfı içe aktarma ve örnekleme değişir.

## LangChain (`langchain-openai`) geçişi

`ChatOpenAI()`'ya `use_responses_api=True` ekleyin. Ayrıca mesaj içerik erişimini `.content`'den `.text`'e güncelleyin.

Önce:
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

# ... ajan çağrısı ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Sonra:
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

# ... ajan çağrısı ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Ana değişiklikler**: (1) Yapıcıda `use_responses_api=True`, (2) yanıt mesajlarında `.content` → `.text`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->