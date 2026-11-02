# Lembaran Cheat API Respons (Python + Azure OpenAI)

> Semua petikan di bawah menganggap `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` dan `client` sudah diinisialisasi (rujuk setup klien).

## Permintaan asas
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Setup klien — EntraID (disyorkan)
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

## Setup klien — Kunci API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Setup klien async — EntraID
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

## Setup klien async — EntraID dengan tenant eksplisit (multi-tenant)

Apabila sumber Azure OpenAI berada dalam **tenant berbeza** daripada default, hantarkan `tenant_id` secara eksplisit ke dalam kredensial. Ini biasa dalam senario dev/test di mana tenant asal pembangun berbeza dengan tenant sumber.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential untuk pengeluaran (Azure Container Apps, App Service, dll.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identiti terurus yang diberikan pengguna
)
# AzureDeveloperCliCredential untuk pembangunan tempatan — tenant_id yang jelas adalah kritikal
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Rantaian: cuba identiti terurus dahulu, kemudian kembali ke azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrasi klien async — sebelum/selepas

Sebelum (ditinggalkan):
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

Selepas:
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

## Migrasi penuh segerak — sebelum/selepas

Sebelum (warisan — Chat Completions Azure OpenAI):
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

Selepas (API Respons — titik hujung Azure OpenAI v1):
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

## Penstriman (segerak)
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
        print()  # baris baru di akhir
```

## Penstriman (async)
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

## Penstriman aplikasi web — bentuk backend-ke-frontend

Semasa migrasi aplikasi web yang menstrim SSE/JSONL ke frontend, **format serialisasi backend** berubah. Reka output backend baru untuk mengekalkan corak akses frontend yang sedia ada supaya frontend tidak memerlukan perubahan.

**Sebelum** — Chat Completions backend biasanya menserial setiap kamus `choices[0]` dalam setiap kepingan:
```python
# Lama: dict pilihan penuh yang diserialkan setiap bahagian
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend baca: `response.delta.content` (laluan dalam objek pilihan).

**Selepas** — Backend API Respons menghantar bentuk minimum yang mengekalkan laluan akses frontend sama:
```python
# Baru: hanya pancarkan apa yang diperlukan oleh frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend masih membaca `response.delta.content` — **tiada perubahan frontend diperlukan**.

> **Pandangan utama**: Bentuk penstriman API Respons (`event.type` + `event.delta`) adalah berbeza secara asas daripada Chat Completions (`chunk.choices[0].delta.content`). Tetapi kontrak backend-ke-frontend adalah hak anda untuk mentakrif. Bentuk output backend supaya sesuai dengan apa yang sudah dijangka frontend.

## Urutan acara penstriman

Apabila `stream: true`, API mengeluarkan acara dalam susunan berikut:
1. `response.created` – objek respons diinisialisasi
2. `response.in_progress` – penjanaan bermula
3. `response.output_item.added` – item output dicipta
4. `response.content_part.added` – bahagian kandungan bermula
5. `response.output_text.delta` – kepingan teks (banyak, setiap satu ada `delta: string`)
6. `response.output_text.done` – penjanaan teks selesai
7. `response.content_part.done` – bahagian kandungan selesai
8. `response.output_item.done` – item output selesai
9. `response.completed` – respons penuh selesai

Untuk penstriman teks asas, hanya kendalikan `response.output_text.delta` (untuk kepingan teks) dan `response.completed` (untuk selesai).

## Pengendalian ralat penstriman dalam aplikasi web

Semasa penstriman dalam aplikasi web, bungkus iterasi async dalam `try/except` dan hasilkan ralat sebagai JSON supaya frontend boleh memaparkannya dengan kemas (cth., had kadar, kegagalan sementara):

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

> **Mengapa ini penting**: Azure OpenAI mengembalikan `429 Too Many Requests` semasa had kadar dikenakan. Tanpa `try/except`, respons penstriman berhenti secara senyap. Dengan ia, frontend menerima `{"error": "Too Many Requests"}` dan boleh menunjukkan galakan cuba semula.

## Jenis acara penstriman (SDK Python)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Format perbualan
```python
# API Respons menyokong format perbualan melalui tatasusunan input
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

## Pengendalian ralat penapis kandungan

Struktur badan ralat berubah daripada Chat Completions ke API Respons.

Sebelum (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Selepas (API Respons):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Perbezaan utama:
- Pembungkus `innererror` adalah **hilang** — butiran penapis kandungan kini pada tahap atas `error.body`.
- `content_filter_result` (tunggal) → `content_filters` (senarai jamak) yang mengandungi `content_filter_results` (jamak) dalam setiap entri.
- Setiap entri dalam `content_filters` termasuk `blocked`, `source_type`, dan `content_filter_results` dengan butiran setiap kategori (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Bentuk badan ralat penapis kandungan penuh API Respons:
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

## Migrasi HTTP mentah (requests/httpx)

Jika aplikasi memanggil REST Azure OpenAI secara langsung daripada SDK:

Sebelum (Chat Completions):
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

Selepas (API Respons):
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

> **Nota**: `output_text` adalah sifat kemudahan pada objek `Response` SDK Python. Respons JSON mentah REST tidak mempunyai medan atas `output_text` — teks berada pada `output[0].content[0].text`.

## Perbualan pelbagai giliran
```python
# Bina perbualan dengan Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Tambah respons pembantu ke dalam perbualan
messages.append({"role": "assistant", "content": response.output_text})

# Teruskan perbualan
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Pelbagai giliran berjenis kandungan (eksplisit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Pelbagai giliran melalui `previous_response_id` (alternatif)

Daripada mengurus array perbualan sendiri, anda boleh kaitkan respons secara
pelayan menggunakan `previous_response_id`. API menyimpan setiap respons dan
secara automatik menambahkan giliran sebelum ini.

```python
# Giliran pertama
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Giliran berikutnya — hanya serahkan mesej pengguna baru + ID respons sebelumnya
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Bila guna yang mana:**

| Pendekatan | Kebaikan | Keburukan |
|---|---|---|
| `input` array (manual) | Kawalan penuh ke atas sejarah; boleh pangkas/ringkaskan; tiada penyimpanan pelayan diperlukan (`store=False`) | Lebih kod; anda urus array |
| `previous_response_id` | Kod lebih mudah; kaitan automatik | Memerlukan `store=True` (default); perbualan disimpan pelayan; tidak boleh ubah sejarah antara giliran |

> **Nota migrasi:** Kebanyakan aplikasi Chat Completions sudah mengurus array mesej sendiri, jadi menukar ke `input` array adalah migrasi 1:1 yang lebih langsung. Gunakan `previous_response_id` untuk kod baru atau bila anda tidak perlu manipulasi sejarah perbualan.

## Model penalaran siri O (o1, o3-mini, o3, o4-mini)

Model siri O mempunyai kekangan parameter unik semasa migrasi ke API Respons.

### Pemetaan parameter untuk siri o

| Chat Completions (siri o) | API Respons | Nota |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Tetapkan tinggi (4096+) — token penalaran dikira terhadap had |
| `reasoning_effort` | `reasoning.effort` | Kekalkan seperti sedia ada jika ada (rendah/sederhana/tinggi) |
| `temperature` | Buang atau tetapkan ke `1` | Siri O hanya terima `1` |
| `top_p` | Buang | Tidak disokong siri o |
| `seed` | Buang | Tidak disokong dalam API Respons |

### Siri O sebelum/selepas

Sebelum (Chat Completions dengan siri o):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Selepas (API Respons):
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

> **Nota**: Model siri O mungkin menyimpan output semasa penalaran sebelum menghantar delta teks. Penstriman masih berfungsi tetapi acara `response.output_text.delta` pertama mungkin datang selepas kelewatan lebih lama berbanding model GPT.

## Mengakses token penalaran
```python
# Model penalaran menggunakan penalaran dalaman — anda boleh melihat berapa banyak token penalaran yang digunakan
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

> **Penting**: Gunakan `max_output_tokens=1000` (bukan 50–200) untuk mengambil kira proses penalaran dalaman model penalaran. Model menggunakan token penalaran secara dalaman sebelum menghasilkan output akhir.

## Output berstruktur — Skema JSON
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

## Penggunaan alat

- Takrifkan fungsi dalam `tools` dengan **format API Respons rata** — `name`, `description`, dan `parameters` di tahap atas (bukan bertingkat di bawah `function`).
- Apabila model meminta panggilan alat, laksanakan dalam aplikasi anda dan termasuk hasil alat dalam permintaan seterusnya sebagai item `function_call_output` dalam `input`.
- Kekalkan skema minimal; sahkan input sebelum laksana.
- Apabila guna `strict: true`, semua sifat mesti disenaraikan dalam `required` dan `additionalProperties: false` wajib.

> **⚠️ `pydantic_function_tool()` tidak serasi**: Pembantu `openai.pydantic_function_tool()` masih menjana format bertingkat lama Chat Completions (`{"type": "function", "function": {"name": ...}}`). Jangan gunakan dengan `responses.create()`. Takrifkan skema alat secara manual atau tulis pembungkus untuk meratakan output.

### Format takrif alat

API Respons menggunakan format alat **rata** — `name`, `description`, `parameters` adalah kunci tahap atas (bukan bertingkat di bawah `function`).

**Sebelum (Chat Completions — bertingkat):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Selepas (API Respons — rata):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Contoh penuh:
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

Dengan `strict: true` (penguatkuasaan skema):
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
            "required": ["city_name"],       # Semua sifat MESTI disenaraikan
            "additionalProperties": False,   # Diperlukan untuk mod ketat
        },
    }
]
```

### Panggilan alat sehala pergi balik (laksanakan dan pulangkan hasil)

Apabila model minta panggilan alat, gunakan item `response.output` + `function_call_output` — **bukan** corak Chat Completions `role: assistant` + `role: tool`.

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
    # Tambah item function_call model ke perbualan
    messages.extend(response.output)

    # Jalankan setiap alat dan tambah keputusan
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Dapatkan respons akhir dengan keputusan alat
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Contoh panggilan alat sedikit

Apabila menyediakan contoh panggilan alat sedikit dalam `input`, gunakan item `function_call` dan `function_call_output`. ID mesti bermula dengan `fc_`.

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
# Contoh carian web terbina dalam
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Input imej

Item kandungan imej menukar jenis daripada `image_url` ke `input_image`, dan URL berubah dari objek bertingkat kepada rentetan rata.

### Input imej — sebelum (Chat Completions)
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

### Input imej — selepas (API Respons, URL)
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

### Input imej — selepas (API Respons, base64)
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

> **Perubahan utama**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (objek bertingkat) → `"image_url": "..."` (rentetan rata — samada URL HTTPS atau `data:image/...;base64,...` URI data), (3) `"type": "text"` → `"type": "input_text"`.

## Migrasi Microsoft Agent Framework (MAF)

**Periksa versi MAF anda dulu** — migrasi bergantung sama ada anda menggunakan MAF 1.0.0+ atau beta/rc sebelum 1.0.0.

Untuk periksa: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Dalam MAF 1.0.0+, `OpenAIChatClient` **sudah menggunakan API Respons** — tiada migrasi diperlukan.

Jika kod menggunakan `OpenAIChatCompletionClient` warisan (yang guna `chat.completions.create`), gantikan dengan `OpenAIChatClient`:

Sebelum:
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

Selepas:
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

### MAF sebelum 1.0.0 (rilis beta/rc)

Dalam MAF sebelum 1.0.0, `OpenAIChatClient` menggunakan Chat Completions. Kemas kini ke `agent-framework-openai>=1.0.0` di mana `OpenAIChatClient` menggunakan API Respons secara lalai.

> **Nota**: `Agent`, `MCPStreamableHTTPTool`, dan API MAF lain kekal tidak berubah — hanya import dan inisialisasi kelas klien yang berubah.

## Migrasi LangChain (`langchain-openai`)

Tambah `use_responses_api=True` ke `ChatOpenAI()`. Juga kemaskini akses kandungan mesej daripada `.content` ke `.text`.

Sebelum:
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

# ... panggilan ejen ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Selepas:
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

# ... panggilan ejen ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Perubahan utama**: (1) `use_responses_api=True` di konstruktor, (2) `.content` → `.text` pada mesej respons.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->