# Responses API Cheat Sheet (Python + Azure OpenAI)

> Όλα τα παρακάτω αποσπάσματα υποθέτουν `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` και ότι ο `client` έχει ήδη αρχικοποιηθεί (βλέπε ρύθμιση client).

## Basic request
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Client setup — EntraID (συνιστάται)
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

## Client setup — API key
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async client setup — EntraID
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

## Async client setup — EntraID με ρητό tenant (multi-tenant)

Όταν το Azure OpenAI resource βρίσκεται σε **διαφορετικό tenant** από το προεπιλεγμένο, δώστε ρητά `tenant_id` στο credential. Αυτό είναι κοινό σε σενάρια ανάπτυξης/δοκιμής όπου ο κύριος tenant του προγραμματιστή διαφέρει από τον tenant του resource.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential για παραγωγή (Azure Container Apps, App Service, κ.λπ.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # διαχειριζόμενη ταυτότητα εκχωρημένη σε χρήστη
)
# AzureDeveloperCliCredential για τοπική ανάπτυξη — το ρητό tenant_id είναι κρίσιμο
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Αλυσίδα: προσπάθησε πρώτα την διαχειριζόμενη ταυτότητα, εναλλακτικά την azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async client migration — πριν/μετά

Πριν (deprecated):
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

Μετά:
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

## Full sync migration — πριν/μετά

Πριν (παλιό — Azure OpenAI Chat Completions):
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

Μετά (Responses API — Azure OpenAI v1 endpoint):
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

## Streaming (sync)
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
        print()  # νέα γραμμή στο τέλος
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

## Web app streaming — δομή backend-to-frontend

Κατά τη μετανάστευση μίας web εφαρμογής που κάνει streaming SSE/JSONL προς frontend, η **μορφή σειριοποίησης backend** αλλάζει. Σχεδιάστε την νέα έξοδο backend ώστε να διατηρεί τα υπάρχοντα μοτίβα πρόσβασης του frontend ώστε να μην απαιτούνται αλλαγές στο frontend.

**Πριν** — Το backend των Chat Completions συχνά σειριοποιούσε το dict `choices[0]` κάθε chunk:
```python
# Παλιό: σειριοποιημένο πλήρες λεξικό επιλογής ανά κομμάτι
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend διαβάζει: `response.delta.content` (βαθιά διαδρομή μέσα στο αντικείμενο επιλογής).

**Μετά** — Το backend του Responses API εκπέμπει μία ελάχιστη μορφή που διατηρεί την ίδια διαδρομή πρόσβασης στο frontend:
```python
# Νέο: εκπέμπει μόνο ό,τι χρειάζεται το frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Το frontend διαβάζει ακόμα `response.delta.content` — **δεν απαιτούνται αλλαγές στο frontend**.

> **Κεντρική ιδέα**: Η μορφή streaming του Responses API (`event.type` + `event.delta`) είναι θεμελιωδώς διαφορετική από των Chat Completions (`chunk.choices[0].delta.content`). Όμως, το συμβόλαιο μεταξύ backend και frontend ορίζεται από εσάς. Σχεδιάστε την έξοδο backend ώστε να ταιριάζει με τις προσδοκίες του frontend.

## Streaming event sequence

Όταν `stream: true`, το API εκπέμπει γεγονότα με αυτή τη σειρά:
1. `response.created` – ξεκίνησε η δημιουργία της απόκρισης
2. `response.in_progress` – η παραγωγή ξεκίνησε
3. `response.output_item.added` – δημιουργήθηκε στοιχείο εξόδου
4. `response.content_part.added` – ξεκίνησε το μέρος περιεχομένου
5. `response.output_text.delta` – κομμάτια κειμένου (πολλαπλά, το καθένα έχει `delta: string`)
6. `response.output_text.done` – ολοκληρώθηκε η παραγωγή κειμένου
7. `response.content_part.done` – ολοκληρώθηκε το μέρος περιεχομένου
8. `response.output_item.done` – ολοκληρώθηκε το στοιχείο εξόδου
9. `response.completed` – ολοκληρώθηκε η πλήρης απόκριση

Για βασικό streaming κειμένου, χειριστείτε μόνο τα `response.output_text.delta` (για κομμάτια κειμένου) και `response.completed` (για το τέλος).

## Streaming error handling σε web apps

Κατά το streaming σε web app, τυλίξτε την ασύγχρονη επανάληψη σε `try/except` και επιστρέψτε σφάλματα ως JSON ώστε το frontend να μπορεί να τα εμφανίσει ομαλά (π.χ., όρια ρυθμού, προσωρινές αποτυχίες):

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

> **Γιατί είναι σημαντικό**: Το Azure OpenAI επιστρέφει `429 Too Many Requests` σε περιορισμό ρυθμού. Χωρίς `try/except`, η ροή απάντησης σταματά χωρίς προειδοποίηση. Με αυτό, το frontend λαμβάνει `{"error": "Too Many Requests"}` και μπορεί να εμφανίσει μήνυμα για επανάληψη.

## Τύποι streaming γεγονότων (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Μορφή συζήτησης
```python
# Η API των Απαντήσεων υποστηρίζει μορφή συνομιλίας μέσω πίνακα εισόδου
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

## Χειρισμός σφαλμάτων φίλτρου περιεχομένου

Η δομή σώματος σφάλματος άλλαξε από Chat Completions σε Responses API.

Πριν (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Μετά (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Κύριες διαφορές:
- Το wrapper `innererror` έχει **αφαιρεθεί** — οι λεπτομέρειες φίλτρου περιεχομένου είναι πλέον στην κορυφή του `error.body`.
- `content_filter_result` (ενικός) → `content_filters` (πληθυντικός πίνακας) που περιλαμβάνει `content_filter_results` (πληθυντικός) μέσα σε κάθε καταχώρηση.
- Κάθε στοιχείο του `content_filters` περιλαμβάνει `blocked`, `source_type`, και `content_filter_results` με λεπτομέρειες ανά κατηγορία (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Πλήρης μορφή σώματος σφάλματος φίλτρου περιεχομένου Responses API:
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

## Μετανάστευση raw HTTP (requests/httpx)

Αν η εφαρμογή καλεί απευθείας το Azure OpenAI REST αντί να χρησιμοποιεί το SDK:

Πριν (Chat Completions):
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

Μετά (Responses API):
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

> **Σημείωση**: Το `output_text` είναι ιδιότητα ευκολίας στο Python SDK `Response` αντικείμενο. Η ακατέργαστη JSON απάντηση REST δεν έχει πεδίο πρώτου επιπέδου `output_text` — το κείμενο βρίσκεται στο `output[0].content[0].text`.

## Πολύστροφες συνομιλίες
```python
# Δημιουργήστε μια συνομιλία με το Responses API
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Προσθέστε την απάντηση του βοηθού στη συνομιλία
messages.append({"role": "assistant", "content": response.output_text})

# Συνεχίστε τη συνομιλία
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Πολύστροφες συνομιλίες με τύπο περιεχομένου (ρητό `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Πολύστροφες με `previous_response_id` (εναλλακτικό)

Αντί να διαχειρίζεστε μόνοι τον πίνακα συνομιλίας, μπορείτε να αλυσιδωτά συνδέσετε απαντήσεις στον server χρησιμοποιώντας `previous_response_id`. Το API αποθηκεύει κάθε απάντηση και προσθέτει αυτόματα τις προηγούμενες στροφές.

```python
# Πρώτη κίνηση
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Επόμενες κινήσεις — απλώς περάστε το νέο μήνυμα χρήστη + το αναγνωριστικό της προηγούμενης απάντησης
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Πότε να χρησιμοποιήσετε ποιο:**

| Προσέγγιση | Πλεονεκτήματα | Μειονεκτήματα |
|---|---|---|
| Πίνακας `input` (χειροκίνητο) | Πλήρης έλεγχος ιστορικού· μπορεί αποκοπή/περίληψη· δεν απαιτεί αποθήκευση/server (`store=False`) | Περισσότερος κώδικας, εσείς διαχειρίζεστε τον πίνακα |
| `previous_response_id` | Απλούστερος κώδικας· αυτόματη αλυσίδα | Απαιτεί `store=True` (προεπιλεγμένο)· η συνομιλία αποθηκεύεται server-side· δεν μπορείτε να τροποποιήσετε το ιστορικό μεταξύ στροφών |

> **Σημείωση μετανάστευσης:** Οι περισσότερες εφαρμογές Chat Completions διαχειρίζονται ήδη τον δικό τους πίνακα μηνυμάτων, οπότε η μετατροπή σε πίνακα `input` είναι πιο ευθύγραμμη μετανάστευση 1:1. Χρησιμοποιήστε `previous_response_id` για νέο κώδικα ή όταν δεν χρειάζεται να χειριστείτε το ιστορικό συνομιλίας.

## Μοντέλα λογικής σειράς O-series (o1, o3-mini, o3, o4-mini)

Τα μοντέλα σειράς O έχουν μοναδικούς περιορισμούς παραμέτρων στη μετανάστευση σε Responses API.

### Αντιστοίχιση παραμέτρων για o-series

| Chat Completions (o-series) | Responses API | Σημειώσεις |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Ορίστε ψηλά (4096+) — τα tokens λογικής μετράνε στο όριο |
| `reasoning_effort` | `reasoning.effort` | Κρατήστε όπως είναι αν υπάρχει (low/medium/high) |
| `temperature` | Αφαιρέστε ή ορίστε σε `1` | Η o-series δέχεται μόνο `1` |
| `top_p` | Αφαιρέστε | Δεν υποστηρίζεται στα o-series |
| `seed` | Αφαιρέστε | Δεν υποστηρίζεται στο Responses API |

### O-series πριν/μετά

Πριν (Chat Completions με o-series):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Μετά (Responses API):
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

> **Σημείωση**: Τα μοντέλα O-series ενδέχεται να αποθηκεύουν προσωρινά έξοδο κατά τη λογική πριν εκπέμψουν τα text deltas. Το streaming λειτουργεί, αλλά το πρώτο `response.output_text.delta` μπορεί να καθυστερήσει περισσότερο σε σχέση με τα μοντέλα GPT.

## Πρόσβαση σε tokens λογικής
```python
# Τα μοντέλα συλλογιστικής χρησιμοποιούν εσωτερική συλλογιστική — μπορείτε να δείτε πόσοι δείκτες συλλογιστικής χρησιμοποιήθηκαν
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

> **Σημαντικό**: Χρησιμοποιήστε `max_output_tokens=1000` (όχι 50–200) για να καλύψετε τη διαδικασία εσωτερικής λογικής των μοντέλων λογικής. Το μοντέλο χρησιμοποιεί tokens λογικής εσωτερικά πριν παραγάγει την τελική έξοδο.

## Δομημένη έξοδος — JSON Schema
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

## Χρήση εργαλείων

- Ορίστε συναρτήσεις στο `tools` με το **επίπεδο (flat) format Responses API** — `name`, `description` και `parameters` στο κορυφαίο επίπεδο (όχι μέσα σε `function`).
- Όταν το μοντέλο ζητά να καλέσει ένα εργαλείο, εκτελέστε το στην εφαρμογή σας και συμπεριλάβετε το αποτέλεσμα στη επόμενη αίτηση ως `function_call_output` στοιχείο μέσα στο `input`.
- Κρατήστε τα σχήματα ελάχιστα· επικυρώστε τις εισόδους πριν την εκτέλεση.
- Όταν χρησιμοποιείτε `strict: true`, όλες οι ιδιότητες πρέπει να αναγράφονται στο `required` και το `additionalProperties: false` είναι υποχρεωτικό.

> **⚠️ Το `pydantic_function_tool()` δεν είναι συμβατό**: Ο βοηθητικός `openai.pydantic_function_tool()` εξακολουθεί να παράγει το παλιό nested format Chat Completions (`{"type": "function", "function": {"name": ...}}`). Μην το χρησιμοποιείτε με `responses.create()`. Ορίστε τα σχήματα εργαλείων χειροκίνητα ή γράψτε wrapper που να "ξεφουσκώνει" την έξοδο.

### Μορφή ορισμού εργαλείων

Το Responses API χρησιμοποιεί **επίπεδη** μορφή εργαλείων — τα `name`, `description`, `parameters` είναι τα κλειδιά πρώτου επιπέδου (όχι μέσα σε `function`).

**Πριν (Chat Completions — nested):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Μετά (Responses API — flat):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Πλήρες παράδειγμα:
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

Με `strict: true` (επιβολή σχήματος):
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
            "required": ["city_name"],       # Όλες οι ιδιότητες ΠΡΕΠΕΙ να αναφέρονται
            "additionalProperties": False,   # Απαιτείται για αυστηρή λειτουργία
        },
    }
]
```

### Κλήση εργαλείου (execute και επαναφορά αποτελεσμάτων)

Όταν το μοντέλο ζητά κλήση εργαλείου, χρησιμοποιήστε τα αντικείμενα `response.output` + `function_call_output` — **όχι** το μοτίβο Chat Completions `role: assistant` + `role: tool`.

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
    # Προσθέστε τα στοιχεία function_call του μοντέλου στη συνομιλία
    messages.extend(response.output)

    # Εκτελέστε κάθε εργαλείο και προσθέστε τα αποτελέσματα
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Λάβετε την τελική απάντηση με τα αποτελέσματα του εργαλείου
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Παραδείγματα λίγων κλήσεων εργαλείου

Κατά την παροχή λίγων παραδειγμάτων κλήσεων εργαλείου στο `input`, χρησιμοποιήστε τα στοιχεία `function_call` και `function_call_output`. Τα IDs πρέπει να αρχίζουν με `fc_`.

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
# Παράδειγμα ενσωματωμένης αναζήτησης ιστού
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Είσοδος εικόνας

Τα αντικείμενα περιεχομένου εικόνας αλλάζουν τύπο από `image_url` σε `input_image`, και το URL αλλάζει από nested αντικείμενο σε επίπεδη συμβολοσειρά.

### Είσοδος εικόνας — πριν (Chat Completions)
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

### Είσοδος εικόνας — μετά (Responses API, URL)
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

### Είσοδος εικόνας — μετά (Responses API, base64)
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

> **Κύριες αλλαγές**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (nested αντικείμενο) → `"image_url": "..."` (επίπεδο string — είτε HTTPS URL είτε `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Μετανάστευση Microsoft Agent Framework (MAF)

**Ελέγξτε πρώτα την έκδοση MAF** — Η μετάβαση εξαρτάται αν είστε σε MAF 1.0.0+ ή σε προ-1.0.0 beta/rc.

Για έλεγχο: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Στην MAF 1.0.0+, το `OpenAIChatClient` **χρησιμοποιεί ήδη το Responses API** — δεν απαιτείται μετάβαση.

Αν ο κώδικας χρησιμοποιεί το παλιό `OpenAIChatCompletionClient` (που καλεί `chat.completions.create`), αντικαταστήστε το με `OpenAIChatClient`:

Πριν:
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

Μετά:
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

### MAF pre-1.0.0 (beta/rc releases)

Σε προ-1.0.0 MAF, το `OpenAIChatClient` χρησιμοποιούσε Chat Completions. Αναβαθμίστε σε `agent-framework-openai>=1.0.0` όπου το `OpenAIChatClient` χρησιμοποιεί από προεπιλογή το Responses API.

> **Σημείωση**: Τα APIs `Agent`, `MCPStreamableHTTPTool`, και άλλα MAF παραμένουν αμετάβλητα — μόνο η εισαγωγή και η δημιουργία instance της κλάσης client αλλάζουν.

## Μετανάστευση LangChain (`langchain-openai`)

Προσθέστε `use_responses_api=True` στο `ChatOpenAI()`. Επίσης, ενημερώστε την πρόσβαση στο περιεχόμενο μηνυμάτων από `.content` σε `.text`.

Πριν:
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

# ... κλήση πράκτορα ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Μετά:
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

# ... κλήση πράκτορα ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Κύριες αλλαγές**: (1) `use_responses_api=True` στο constructor, (2) `.content` → `.text` στα μηνύματα απάντησης.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->