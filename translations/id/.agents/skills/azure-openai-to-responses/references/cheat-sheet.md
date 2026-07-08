# Cheat Sheet API Responses (Python + Azure OpenAI)

> Semua cuplikan di bawah menganggap `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` dan `client` sudah diinisialisasi (lihat pengaturan klien).

## Permintaan dasar
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Pengaturan klien — EntraID (disarankan)
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

## Pengaturan klien — Kunci API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Pengaturan klien async — EntraID
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

## Pengaturan klien async — EntraID dengan tenant eksplisit (multi-tenant)

Saat sumber daya Azure OpenAI berada di **tenant berbeda** dari default, berikan `tenant_id` secara eksplisit ke kredensial. Ini umum dalam skenario dev/test di mana tenant home developer berbeda dari tenant sumber daya.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential untuk produksi (Azure Container Apps, App Service, dll.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # identitas terkelola yang ditugaskan pengguna
)
# AzureDeveloperCliCredential untuk pengembangan lokal — tenant_id eksplisit sangat penting
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Rantai: coba identitas terkelola terlebih dahulu, kembali ke CLI azd
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Migrasi klien async — sebelum/sesudah

Sebelum (tidak direkomendasikan):
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

Sesudah:
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

## Migrasi sinkron penuh — sebelum/sesudah

Sebelum (legacy — Azure OpenAI Chat Completions):
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

Sesudah (Responses API — endpoint Azure OpenAI v1):
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

## Streaming (sinkron)
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

## Streaming (async)
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

## Streaming aplikasi web — bentuk backend-ke-frontend

Saat memigrasi aplikasi web yang streaming SSE/JSONL ke frontend, **format serialisasi backend** berubah. Rancang output backend baru agar mempertahankan pola akses frontend yang sudah ada sehingga frontend tidak perlu diubah.

**Sebelum** — Backend Chat Completions biasanya melakukan serialisasi kamus `choices[0]` setiap chunk:
```python
# Lama: dict pilihan penuh yang diserialisasi per chunk
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend membaca: `response.delta.content` (jalur dalam objek choice).

**Sesudah** — Backend Responses API mengeluarkan bentuk minimal yang mempertahankan jalur akses frontend yang sama:
```python
# Baru: keluarkan hanya apa yang dibutuhkan frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend masih membaca `response.delta.content` — **tidak perlu perubahan frontend**.

> **Wawasan utama**: Bentuk streaming Responses API (`event.type` + `event.delta`) secara fundamental berbeda dari Chat Completions (`chunk.choices[0].delta.content`). Namun kontrak backend-ke-frontend adalah milik Anda untuk menentukan. Bentuklah output backend agar sesuai dengan yang sudah diharapkan frontend.

## Urutan event streaming

Saat `stream: true`, API mengeluarkan event dalam urutan ini:
1. `response.created` – objek respons diinisialisasi
2. `response.in_progress` – generasi dimulai
3. `response.output_item.added` – item output dibuat
4. `response.content_part.added` – bagian konten dimulai
5. `response.output_text.delta` – potongan teks (multi, masing-masing dengan `delta: string`)
6. `response.output_text.done` – generasi teks selesai
7. `response.content_part.done` – bagian konten selesai
8. `response.output_item.done` – item output selesai
9. `response.completed` – respons penuh selesai

Untuk streaming teks dasar, tangani hanya `response.output_text.delta` (potongan teks) dan `response.completed` (untuk selesai).

## Penanganan kesalahan streaming di aplikasi web

Saat streaming di aplikasi web, bungkus iterasi async dalam `try/except` dan hasilkan kesalahan sebagai JSON agar frontend dapat menampilkannya dengan baik (misalnya, batas laju, kegagalan sementara):

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

> **Mengapa ini penting**: Azure OpenAI mengembalikan `429 Too Many Requests` saat pembatasan laju. Tanpa `try/except`, respons streaming mati tanpa suara. Dengan itu, frontend menerima `{"error": "Too Many Requests"}` dan dapat menampilkan prompt coba ulang.

## Jenis event streaming (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Format percakapan
```python
# API Respon mendukung format percakapan melalui array input
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

## Penanganan kesalahan filter konten

Struktur badan kesalahan berubah dari Chat Completions ke Responses API.

Sebelum (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Sesudah (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Perbedaan utama:
- Wrapper `innererror` **hilang** — detail filter konten kini berada di tingkat atas `error.body`.
- `content_filter_result` (tunggal) → `content_filters` (array jamak) yang berisi `content_filter_results` (jamak) di setiap entri.
- Setiap entri dalam `content_filters` berisi `blocked`, `source_type`, dan `content_filter_results` dengan detail per kategori (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Bentuk badan kesalahan filter konten Responses API lengkap:
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

Jika aplikasi memanggil Azure OpenAI REST langsung tanpa SDK:

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

Sesudah (Responses API):
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

> **Catatan**: `output_text` adalah properti kemudahan pada objek `Response` Python SDK. Respons JSON REST mentah tidak memiliki field top-level `output_text` — teks berada di `output[0].content[0].text`.

## Percakapan multi-putar
```python
# Bangun percakapan dengan Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Tambahkan balasan asisten ke percakapan
messages.append({"role": "assistant", "content": response.output_text})

# Lanjutkan percakapan
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Multi-putar bertipe konten (eksplicit `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Multi-putar via `previous_response_id` (alternatif)

Alih-alih mengelola array percakapan sendiri, Anda dapat menghubungkan respons
di sisi server menggunakan `previous_response_id`. API menyimpan setiap respons dan
otomatis menambahkan putaran sebelumnya.

```python
# Giliran pertama
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Giliran berikutnya — cukup teruskan pesan pengguna baru + ID respons sebelumnya
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Kapan menggunakan yang mana:**

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Array `input` (manual) | Kontrol penuh atas histori; dapat memangkas/merangkum; tidak perlu penyimpanan server (`store=False`) | Lebih banyak kode; Anda mengelola array |
| `previous_response_id` | Kode lebih sederhana; chaining otomatis | Memerlukan `store=True` (default); percakapan tersimpan di server; tidak dapat mengubah histori antar putaran |

> **Catatan migrasi:** Sebagian besar aplikasi Chat Completions sudah mengelola array pesan sendiri, jadi konversi ke array `input` adalah migrasi 1:1 yang lebih langsung. Gunakan `previous_response_id` untuk kode baru atau jika Anda tidak perlu memanipulasi histori percakapan.

## Model penalaran seri O (o1, o3-mini, o3, o4-mini)

Model seri O memiliki keterbatasan parameter unik saat migrasi ke Responses API.

### Pemetaan parameter untuk seri O

| Chat Completions (seri O) | Responses API | Catatan |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Atur tinggi (4096+) — token penalaran dihitung dalam batas |
| `reasoning_effort` | `reasoning.effort` | Pertahankan seperti adanya jika ada (rendah/sedang/tinggi) |
| `temperature` | Hapus atau atur ke `1` | Seri O hanya menerima `1` |
| `top_p` | Hapus | Tidak didukung pada seri O |
| `seed` | Hapus | Tidak didukung di Responses API |

### Seri O sebelum/sesudah

Sebelum (Chat Completions dengan seri O):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Sesudah (Responses API):
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

> **Catatan**: Model seri O mungkin menyimpan keluaran selama penalaran sebelum mengeluarkan delta teks. Streaming masih berfungsi tapi event pertama `response.output_text.delta` mungkin datang setelah jeda lebih lama dibandingkan model GPT.

## Mengakses token penalaran
```python
# Model penalaran menggunakan penalaran internal — Anda dapat melihat berapa banyak token penalaran yang digunakan
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

> **Penting**: Gunakan `max_output_tokens=1000` (bukan 50–200) untuk mengakomodasi proses internal model penalaran. Model menggunakan token penalaran secara internal sebelum menghasil keluaran akhir.

## Output terstruktur — Skema JSON
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

- Definisikan fungsi di `tools` dengan **format flat Responses API** — `name`, `description`, dan `parameters` di level atas (tidak bersarang di bawah `function`).
- Saat model meminta panggilan alat, jalankan di aplikasi Anda dan sertakan hasil alat di permintaan berikutnya sebagai item `function_call_output` dalam `input`.
- Jaga skema tetap minimal; validasi input sebelum eksekusi.
- Saat menggunakan `strict: true`, semua properti harus tercantum dalam `required` dan `additionalProperties: false` wajib.

> **⚠️ `pydantic_function_tool()` tidak kompatibel**: Helper `openai.pydantic_function_tool()` masih menghasilkan format bersarang Chat Completions lama (`{"type": "function", "function": {"name": ...}}`). Jangan gunakan dengan `responses.create()`. Definisikan skema alat secara manual atau buat wrapper untuk membuat output menjadi flat.

### Format definisi alat

Responses API menggunakan format alat **flat** — `name`, `description`, `parameters` adalah kunci level atas (tidak bersarang di bawah `function`).

**Sebelum (Chat Completions — bersarang):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Sesudah (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Contoh lengkap:
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

Dengan `strict: true` (penegakan skema):
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
            "required": ["city_name"],       # Semua properti HARUS dicantumkan
            "additionalProperties": False,   # Diperlukan untuk mode ketat
        },
    }
]
```

### Round-trip panggilan alat (jalankan dan kembalikan hasil)

Saat model meminta panggilan alat, gunakan item `response.output` + `function_call_output` — **bukan** pola Chat Completions `role: assistant` + `role: tool`.

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
    # Tambahkan item function_call model ke percakapan
    messages.extend(response.output)

    # Jalankan setiap alat dan tambahkan hasilnya
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Dapatkan respons akhir dengan hasil alat
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Contoh panggilan alat few-shot

Saat menyediakan contoh panggilan alat few-shot dalam `input`, gunakan item `function_call` dan `function_call_output`. ID harus diawali dengan `fc_`.

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
# Contoh pencarian web bawaan
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Input gambar

Item konten gambar mengubah tipe dari `image_url` menjadi `input_image`, dan URL berubah dari objek bersarang menjadi string flat.

### Input gambar — sebelum (Chat Completions)
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

### Input gambar — sesudah (Responses API, URL)
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

### Input gambar — sesudah (Responses API, base64)
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

> **Perubahan utama**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (objek bersarang) → `"image_url": "..."` (string flat — URL HTTPS atau URI data `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Migrasi Microsoft Agent Framework (MAF)

**Periksa versi MAF Anda terlebih dahulu** — migrasi tergantung pada apakah Anda menggunakan MAF 1.0.0+ atau beta/rc pra-1.0.0.

Untuk memeriksa: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Pada MAF 1.0.0+, `OpenAIChatClient` **sudah menggunakan Responses API** — tidak perlu migrasi.

Jika basis kode menggunakan `OpenAIChatCompletionClient` lama (yang memakai `chat.completions.create`), ganti dengan `OpenAIChatClient`:

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

Sesudah:
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

### MAF pra-1.0.0 (rilis beta/rc)

Pada MAF pra-1.0.0, `OpenAIChatClient` menggunakan Chat Completions. Tingkatkan ke `agent-framework-openai>=1.0.0` di mana `OpenAIChatClient` menggunakan Responses API secara default.

> **Catatan**: API `Agent`, `MCPStreamableHTTPTool`, dan lainnya di MAF tetap tidak berubah — hanya impor dan instansiasi kelas klien yang berubah.

## Migrasi LangChain (`langchain-openai`)

Tambahkan `use_responses_api=True` ke `ChatOpenAI()`. Juga perbarui akses konten pesan dari `.content` menjadi `.text`.

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

# ... pemanggilan agen ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Sesudah:
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

# ... pemanggilan agen ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Perubahan kunci**: (1) `use_responses_api=True` di konstruktor, (2) `.content` → `.text` pada pesan respons.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->