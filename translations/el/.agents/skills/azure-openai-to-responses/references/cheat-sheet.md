# Φύλλο Απαραίτητων Απαντήσεων API (Python + Azure OpenAI)

> Όλα τα παρακάτω αποσπάσματα υποθέτουν `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` και το `client` είναι ήδη αρχικοποιημένο (βλ. ρύθμιση client).

## Βασικό αίτημα
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Ρύθμιση client — EntraID (συνιστάται)
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

## Ρύθμιση client — Κλειδί API
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Ασύγχρονη ρύθμιση client — EntraID
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

## Ασύγχρονη ρύθμιση client — EntraID με ρητό tenant (πολυενοικιακότητα)

Όταν ο πόρος Azure OpenAI είναι σε **διαφορετικό tenant** από το προεπιλεγμένο, περάστε ρητά `tenant_id` στο διαπιστευτήριο. Αυτό είναι κοινό σε σενάρια ανάπτυξης/δοκιμής όπου ο κύριος tenant του προγραμματιστή διαφέρει από τον tenant του πόρου.

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
    client_id=os.getenv("AZURE_CLIENT_ID")  # διαχειριζόμενη ταυτότητα που έχει ανατεθεί από τον χρήστη
)
# AzureDeveloperCliCredential για τοπική ανάπτυξη — η ρητή tenant_id είναι κρίσιμη
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Αλυσίδα: δοκιμάστε πρώτα την διαχειριζόμενη ταυτότητα, αν αποτύχει επιστροφή στο azd CLI
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Μεταφορά ασύγχρονου client — πριν/μετά

Πριν (καταργημένο):
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

## Πλήρης συγχρονισμένη μεταφορά — πριν/μετά

Πριν (παλαιό — Azure OpenAI Chat Completions):
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

Μετά (Responses API — σημείο τέλους Azure OpenAI v1):
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

## Ροή δεδομένων (συγχρονισμένη)
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

## Ροή δεδομένων (ασύγχρονη)
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

## Ροή εφαρμογής ιστού — μορφή backend προς frontend

Κατά τη μεταφορά εφαρμογής ιστού που πραγματοποιεί ροή SSE/JSONL προς frontend, η **μορφή ακολουθίας backend** αλλάζει. Σχεδιάστε το νέο backend για να διατηρήσετε τα υπάρχοντα μοτίβα πρόσβασης του frontend ώστε να μην απαιτούνται αλλαγές στο frontend.

**Πριν** — Το backend του Chat Completions συνήθως σειριοποιούσε το λεξικό `choices[0]` κάθε τμήματος:
```python
# Παλαιό: σειριοποιημένο πλήρες λεξικό επιλογής ανά κομμάτι
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend ανάγνωση: `response.delta.content` (βαθιά διαδρομή στο αντικείμενο επιλογής).

**Μετά** — Το backend του Responses API εκπέμπει μια μινιμαλιστική μορφή διατηρώντας την ίδια πρόσβαση frontend:
```python
# Νέο: εκπέμψτε μόνο ό,τι χρειάζεται το frontend
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Το frontend εξακολουθεί να διαβάζει `response.delta.content` — **δεν απαιτούνται αλλαγές frontend**.

> **Κύριο συμπέρασμα**: Η μορφή ροής του Responses API (`event.type` + `event.delta`) διαφέρει θεμελιωδώς από το Chat Completions (`chunk.choices[0].delta.content`). Αλλά το συμβόλαιο backend προς frontend το ορίζετε εσείς. Μορφοποιήστε την έξοδο backend ώστε να ταιριάζει με τις προβλέψεις του frontend.

## Αλληλουχία γεγονότων ροής

Όταν `stream: true`, η API εκπέμπει γεγονότα με αυτή τη σειρά:
1. `response.created` – αντικείμενο απάντησης αρχικοποιήθηκε
2. `response.in_progress` – η δημιουργία ξεκίνησε
3. `response.output_item.added` – δημιουργήθηκε στοιχείο εξόδου
4. `response.content_part.added` – ξεκίνησε το μέρος του περιεχομένου
5. `response.output_text.delta` – τμήματα κειμένου (πολλαπλά, το καθένα έχει `delta: string`)
6. `response.output_text.done` – ολοκληρώθηκε η δημιουργία κειμένου
7. `response.content_part.done` – ολοκληρώθηκε το μέρος περιεχομένου
8. `response.output_item.done` – ολοκληρώθηκε το στοιχείο εξόδου
9. `response.completed` – ολοκληρώθηκε πλήρως η απάντηση

Για απλή ροή κειμένου, χειριστείτε μόνο το `response.output_text.delta` (για τμήματα κειμένου) και το `response.completed` (για το τέλος).

## Χειρισμός σφαλμάτων ροής σε εφαρμογές ιστού

Κατά τη ροή σε εφαρμογή ιστού, τυλίξτε την ασύγχρονη επανάληψη με `try/except` και επιστρέψτε σφάλματα ως JSON ώστε το frontend να μπορεί να τα εμφανίσει ομαλά (π.χ., όρια ρυθμού, προσωρινές αποτυχίες):

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

> **Γιατί έχει σημασία**: Το Azure OpenAI επιστρέφει `429 Too Many Requests` κατά τον περιορισμό ρυθμού. Χωρίς το `try/except`, η ροή απάντησης τερματίζει σιωπηλά. Με αυτό, το frontend λαμβάνει `{"error": "Too Many Requests"}` και μπορεί να εμφανίσει αίτημα επανάληψης.

## Τύποι γεγονότων ροής (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Μορφή διαλόγου
```python
# Το API Απαντήσεων υποστηρίζει μορφή συνομιλίας μέσω πίνακα εισόδου
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

Βασικές διαφορές:
- Το περιτύλιγμα `innererror` **λείπει** — οι λεπτομέρειες φίλτρου περιεχομένου τώρα βρίσκονται στο ανώτερο επίπεδο του `error.body`.
- Το `content_filter_result` (ενικός) έγινε `content_filters` (πληθυντικός πίνακας) που περιέχει `content_filter_results` (πληθυντικός) μέσα σε κάθε είσοδο.
- Κάθε είσοδος στα `content_filters` περιλαμβάνει `blocked`, `source_type`, και `content_filter_results` με λεπτομέρειες ανά κατηγορία (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Πλήρης μορφή σώματος σφαλμάτων φίλτρου περιεχομένου Responses API:
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

## Ακατέργαστη μεταφορά HTTP (requests/httpx)

Αν η εφαρμογή καλεί απευθείας Azure OpenAI REST αντί να χρησιμοποιεί το SDK:

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

> **Σημείωση**: Το `output_text` είναι ιδιότητα ευκολίας στο αντικείμενο `Response` της Python SDK. Η ακατέργαστη JSON απάντηση REST δεν έχει πεδίο `output_text` στην κορυφή — το κείμενο βρίσκεται στο `output[0].content[0].text`.

## Πολλαπλός γύρος διαλόγου
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

Πολλαπλού γύρου με τύπους περιεχομένου (ρητό `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Πολλαπλός γύρος μέσω `previous_response_id` (εναλλακτικό)

Αντί να διαχειρίζεστε τον πίνακα διαλόγου εσείς, μπορείτε να αλυσιδωτές απαντήσεις
από την πλευρά του διακομιστή χρησιμοποιώντας `previous_response_id`. Η API αποθηκεύει κάθε απάντηση και
προσθέτει αυτόματα τις προηγούμενες γύρους.

```python
# Πρώτη κίνηση
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Επόμενες κινήσεις — απλώς δώστε το νέο μήνυμα χρήστη + το προηγούμενο ID απόκρισης
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Πότε να χρησιμοποιείτε τι:**

| Προσέγγιση | Πλεονεκτήματα | Μειονεκτήματα |
|---|---|---|
| Πίνακας `input` (χειροκίνητος) | Πλήρης έλεγχος ιστορικού· δυνατότητα κοπής/συνοψίσεων· δεν χρειάζεται αποθήκευση στον διακομιστή (`store=False`) | Περισσότερος κώδικας· εσείς διαχειρίζεστε τον πίνακα |
| `previous_response_id` | Απλούστερος κώδικας· αυτόματη αλυσιδωτή σύνδεση | Απαιτεί `store=True` (προεπιλογή)· ο διάλογος αποθηκεύεται στον διακομιστή· δεν μπορεί να τροποποιηθεί το ιστορικό μεταξύ γύρων |

> **Σημείωση μεταφοράς:** Οι περισσότερες εφαρμογές Chat Completions ήδη διαχειρίζονται τον δικό τους πίνακα μηνυμάτων, οπότε η μετάβαση σε πίνακα `input` είναι πιο άμεση μεταφορά 1:1. Χρησιμοποιήστε `previous_response_id` σε νέο κώδικα ή όταν δεν χρειάζεται να τροποποιήσετε το ιστορικό διαλόγου.

## Μοντέλα ορθολογισμού σειράς O (o1, o3-mini, o3, o4-mini)

Τα μοντέλα σειράς O έχουν μοναδικούς περιορισμούς παραμέτρων κατά τη μεταφορά στο Responses API.

### Αντιστοίχιση παραμέτρων για σειρά O

| Chat Completions (σειρά O) | Responses API | Σημειώσεις |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Ορίστε υψηλή τιμή (4096+) — τα tokens ορθολογισμού μετράνε στο όριο |
| `reasoning_effort` | `reasoning.effort` | Κρατήστε όπως είναι αν υπάρχει (χαμηλό/μεσαίο/υψηλό) |
| `temperature` | Αφαιρέστε ή ορίστε σε `1` | Η σειρά O δέχεται μόνο `1` |
| `top_p` | Αφαιρέστε | Δεν υποστηρίζεται στη σειρά O |
| `seed` | Αφαιρέστε | Δεν υποστηρίζεται στο Responses API |

### Σειρά O πριν/μετά

Πριν (Chat Completions με σειρά O):
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

> **Σημείωση**: Τα μοντέλα σειράς O μπορεί να συγκρατούν έξοδο κατά τη διαδικασία ορθολογισμού πριν εκπέμψουν διαφορές κειμένου. Η ροή λειτουργεί ακόμα αλλά το πρώτο γεγονός `response.output_text.delta` μπορεί να φτάσει μετά από μεγαλύτερη καθυστέρηση σε σχέση με τα μοντέλα GPT.

## Πρόσβαση σε tokens ορθολογισμού
```python
# Τα μοντέλα συλλογισμού χρησιμοποιούν εσωτερική λογική — μπορείτε να δείτε πόσα tokens συλλογισμού χρησιμοποιήθηκαν
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

> **Σημαντικό**: Χρησιμοποιήστε `max_output_tokens=1000` (όχι 50–200) για να καλύψετε την εσωτερική διαδικασία ορθολογισμού των μοντέλων. Το μοντέλο χρησιμοποιεί tokens ορθολογισμού πριν παραγάγει την τελική έξοδο.

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

- Ορίστε συναρτήσεις στο `tools` με τη **επίπεδη μορφή Responses API** — `name`, `description`, και `parameters` σε ανώτατο επίπεδο (όχι μέσα σε `function`).
- Όταν το μοντέλο ζητήσει να καλέσει εργαλείο, εκτελέστε το στην εφαρμογή σας και συμπεριλάβετε το αποτέλεσμα εργαλείου στο επόμενο αίτημα ως `function_call_output` μέσα στο `input`.
- Κρατήστε τα σχήματα ελάχιστα· επικυρώστε τις εισόδους πριν την εκτέλεση.
- Όταν χρησιμοποιείτε `strict: true`, όλες οι ιδιότητες πρέπει να είναι στη λίστα `required` και απαιτείται `additionalProperties: false`.

> **⚠️ Η `pydantic_function_tool()` δεν είναι συμβατή**: Ο βοηθός `openai.pydantic_function_tool()` παράγει ακόμα την παλιά εμφωλευμένη μορφή του Chat Completions (`{"type": "function", "function": {"name": ...}}`). Μην τη χρησιμοποιείτε με `responses.create()`. Ορίστε τα σχήματα εργαλείων χειροκίνητα ή γράψτε wrapper για να επίπεδοποιήσετε την έξοδο.

### Μορφή ορισμού εργαλείου

Το Responses API χρησιμοποιεί **επίπεδη** μορφή εργαλείου — `name`, `description`, `parameters` είναι κλειδιά ανώτατου επιπέδου (όχι μέσα σε `function`).

**Πριν (Chat Completions — εμφωλευμένα):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Μετά (Responses API — επίπεδα):**
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

### Περίπτωση κλήσης εργαλείου (εκτέλεση και επιστροφή αποτελεσμάτων)

Όταν το μοντέλο ζητά κλήση εργαλείου, χρησιμοποιήστε τα `response.output` + `function_call_output` — **όχι** το μοτίβο Chat Completions `role: assistant` + `role: tool`.

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

    # Λάβετε την τελική απάντηση με τα αποτελέσματα των εργαλείων
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Παραδείγματα κλήσεων εργαλείου με λίγα δείγματα

Όταν παρέχετε λίγα δείγματα κλήσεων εργαλείων στο `input`, χρησιμοποιείτε τα αντικείμενα `function_call` και `function_call_output`. Τα αναγνωριστικά πρέπει να ξεκινούν με `fc_`.

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
# Παράδειγμα ενσωματωμένης διαδικτυακής αναζήτησης
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Είσοδος εικόνας

Τα στοιχεία περιεχομένου εικόνας αλλάζουν τύπο από `image_url` σε `input_image`, και το URL αλλάζει από εμφωλευμένο αντικείμενο σε απλό string.

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

> **Βασικές αλλαγές**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (εμφωλευμένο αντικείμενο) → `"image_url": "..."` (επίπεδο string — είτε HTTPS URL είτε URI δεδομένων `data:image/...;base64,...`), (3) `"type": "text"` → `"type": "input_text"`.

## Μεταφορά Microsoft Agent Framework (MAF)

**Ελέγξτε πρώτα την έκδοση MAF** — η μεταφορά εξαρτάται αν είστε στο MAF 1.0.0+ ή σε προ-1.0.0 beta/rc.

Για έλεγχο: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Στο MAF 1.0.0+, το `OpenAIChatClient` **χρησιμοποιεί ήδη το Responses API** — δεν απαιτείται μεταφορά.

Αν ο κώδικας χρησιμοποιεί το παλιό `OpenAIChatCompletionClient` (που χρησιμοποιεί το `chat.completions.create`), αντικαταστήστε το με `OpenAIChatClient`:

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

### MAF προ-1.0.0 (beta/rc εκδόσεις)

Στο προ-1.0.0 MAF, το `OpenAIChatClient` χρησιμοποιούσε Chat Completions. Αναβαθμίστε σε `agent-framework-openai>=1.0.0` όπου το `OpenAIChatClient` χρησιμοποιεί εξ ορισμού το Responses API.

> **Σημείωση**: Οι APIs `Agent`, `MCPStreamableHTTPTool` και άλλες του MAF παραμένουν αμετάβλητες — μόνο η εισαγωγή και η δημιουργία του client αλλάζουν.

## Μεταφορά LangChain (`langchain-openai`)

Προσθέστε `use_responses_api=True` στο `ChatOpenAI()`. Ενημερώστε επίσης την πρόσβαση στο περιεχόμενο μηνυμάτων από `.content` σε `.text`.

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

> **Βασικές αλλαγές**: (1) `use_responses_api=True` στον κατασκευαστή, (2) `.content` → `.text` στα μηνύματα απάντησης.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->