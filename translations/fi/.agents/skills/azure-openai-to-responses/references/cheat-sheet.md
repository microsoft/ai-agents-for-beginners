# Responses API Pikalinkkivihko (Python + Azure OpenAI)

> Kaikki alla olevat koodiesimerkit olettavat `deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` ja että `client` on jo alustettu (katso clientin asetukset).

## Peruspyyntö
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## Clientin asennus — EntraID (suositeltu)
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

## Clientin asennus — API-avain
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async clientin asennus — EntraID
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

## Async clientin asennus — EntraID eksplisiittisellä vuokralla (multi-tenant)

Kun Azure OpenAI -resurssi on **eri vuokralaissa** kuin oletusvuokra, anna `tenant_id` suoraan tunnistetiedoille. Tämä on yleistä kehitys/testausympäristöissä, joissa kehittäjän kotivuokra eroaa resurssin vuokrasta.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential tuotantokäyttöön (Azure Container Apps, App Service, ym.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # käyttäjän määrittämä managed identity
)
# AzureDeveloperCliCredential paikalliseen kehitykseen — eksplisiittinen tenant_id on kriittinen
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ketju: yritä ensin managed identityä, siirry sitten azd CLI:hin
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## Async clientin siirtymä — ennen/jälkeen

Ennen (vanhentunut):
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

Jälkeen:
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

## Täysimittainen synkroninen siirtymä — ennen/jälkeen

Ennen (perinteinen — Azure OpenAI Chat Completions):
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

Jälkeen (Responses API — Azure OpenAI v1 -päätepiste):
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

## Suoratoisto (synkroninen)
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
        print()  # rivinvaihto lopussa
```

## Suoratoisto (asynkroninen)
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

## Web-sovelluksen suoratoisto — taustapalvelimelta frontendiin

Kun siirrät web-sovellusta, joka suoratoistaa SSE/JSONL-frontendiin, **taustapalvelimen sarjoitusmuoto** muuttuu. Suunnittele uusi taustatuloste säilyttämään frontendin nykyiset käyttökuviot, jotta frontendiin ei tarvitse tehdä muutoksia.

**Ennen** — Chat Completions -taustapalvelin jäsenteli tyypillisesti kunkin palan `choices[0]` sanakirjan:
```python
# Vanha: sarjattu koko valintasanakirja per lohko
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend lukee: `response.delta.content` (syvä polku valintaan).

**Jälkeen** — Responses API:n taustapalvelin lähettää minimalistisen rakenteen säilyttäen saman frontendin käyttöpolun:
```python
# Uusi: tuota vain se, mitä käyttöliittymä tarvitsee
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend lukee edelleen `response.delta.content` — **ei tarvita muutoksia frontendissä**.

> **Keskeinen huomio**: Responses API:n suoratoistorakenne (`event.type` + `event.delta`) on perustavanlaatuisesti erilainen kuin Chat Completions (`chunk.choices[0].delta.content`). Mutta sinun taustapalvelin-frontendi -sopimuksesi on sinun määriteltävissäsi. Muotoile taustatuloste vastaamaan frontendin odotuksia.

## Suoratoisto tapahtumasarja

Kun `stream: true`, API lähettää tapahtumat tässä järjestyksessä:
1. `response.created` – vastausobjekti alustettu
2. `response.in_progress` – generaation aloitus
3. `response.output_item.added` – tulososa luotu
4. `response.content_part.added` – sisältöosa aloitettu
5. `response.output_text.delta` – tekstipalat (useita, jokaisella `delta: string`)
6. `response.output_text.done` – tekstin generointi valmis
7. `response.content_part.done` – sisältöosa valmis
8. `response.output_item.done` – tulososa valmis
9. `response.completed` – koko vastaus valmis

Perustekstin suoratoistossa käsittele vain `response.output_text.delta` (tekstipalat) ja `response.completed` (valmistuminen).

## Suoratoiston virheenkäsittely web-sovelluksissa

Suoratoiston yhteydessä web-sovelluksessa kiedo asynkroninen iteraatio `try/except`-rakenteeseen ja palauta virheet JSON-muodossa, jotta frontendi voi näyttää ne siististi (esim. käyttörajoitukset, tilapäiset virheet):

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

> **Miksi tämä on tärkeää**: Azure OpenAI palauttaa `429 Too Many Requests` käyttörajoitusten aikana. Ilman `try/except`-lohkkoa suoratoistovastaus lopettaa hiljaa toiminnan. Sen kanssa frontend saa `{"error": "Too Many Requests"}` ja voi näyttää uudelleenyrityskehotteen.

## Suoratoiston tapahtumatyypit (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Keskustelun formaatti
```python
# Vastaukset API tukee keskustelumuotoa syöte-taulukon avulla
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

## Sisällönsuodatinvirheiden käsittely

Virheen rungon rakenne muuttui Chat Completionsista Responses APIin.

Ennen (Chat Completions):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Jälkeen (Responses API):
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

Keskeiset erot:
- `innererror`-kääre on **poistettu** — sisällönsuodattimen tiedot ovat nyt virheen rungon ylimmällä tasolla `error.body`.
- `content_filter_result` (yksikkö) → `content_filters` (monikko-taulukko), joka sisältää `content_filter_results` (monikko) jokaisessa kohdassa.
- Jokainen `content_filters`-taulukon kohta sisältää `blocked`, `source_type` ja `content_filter_results`, joissa on kategoriset tiedot (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Täysi Responses API -sisällönsuodatinvirheen rungon muoto:
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

## Raaka HTTP-siirtymä (requests/httpx)

Jos sovellus kutsuu Azure OpenAI RESTiä suoraan SDK:n sijaan:

Ennen (Chat Completions):
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

Jälkeen (Responses API):
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

> **Huom**: `output_text` on kätevyysominaisuus Python SDK:n `Response`-objektissa. Raakaa REST JSON -vastausta ei ole ylimpänä kenttänä `output_text` — teksti löytyy `output[0].content[0].text`-polusta.

## Monikierroksinen keskustelu
```python
# Rakenna keskustelu Responses API:lla
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# Lisää avustajan vastaus keskusteluun
messages.append({"role": "assistant", "content": response.output_text})

# Jatka keskustelua
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

Sisältötyyppinen monikierros (eksplisiittinen `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Monikierros käyttäen `previous_response_id` (vaihtoehto)

Sen sijaan, että hallitsisit keskustelun taulukkoa itse, voit ketjuttaa vastauksia
palvelinpuolella käyttäen `previous_response_id`:tä. API tallentaa jokaisen vastauksen ja
lisää automaattisesti edelliset kierrokset mukaan.

```python
# Ensimmäinen vuoro
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Seuraavat vuorot — lähetä vain uusi käyttäjäviesti + edellisen vastauksen tunniste
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Milloin käyttää mitä:**

| Lähestymistapa | Edut | Haitat |
|---|---|---|
| `input`-taulukko (manuaalinen) | Täysi hallinta historiasta; voi rajata/yhdistellä; ei tarvita palvelintallennusta (`store=False`) | Lisää koodia; sinun pitää hallita taulukkoa |
| `previous_response_id` | Yksinkertaisempi koodi; automaattinen ketjutus | Vaatii `store=True` (oletus); keskustelu tallennetaan palvelimella; historiaa ei voi muuttaa kierrosten välillä |

> **Muutoshuomio:** Useimmat Chat Completions -sovellukset hallitsevat itse viestitaulukkoa, joten siirtyminen `input`-taulukkoon on suoraviivainen 1:1-muutos. Käytä `previous_response_id`:tä uudessa koodissa tai kun keskusteluhistoriaa ei tarvitse muokata.

## O-sarjan päättelymallit (o1, o3-mini, o3, o4-mini)

O-sarjan malleilla on ainutlaatuisia parametrirajoitteita siirryttäessä Responses APIin.

### Parametrien kartoitus o-sarjalle

| Chat Completions (o-sarja) | Responses API | Huomiot |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Aseta korkeaksi (4096+) — päättelytokenit lasketaan mukaan |
| `reasoning_effort` | `reasoning.effort` | Säilytä ennallaan jos on (low/medium/high) |
| `temperature` | Poista tai aseta `1` | O-sarja hyväksyy vain arvon `1` |
| `top_p` | Poista | Ei tuettu o-sarjassa |
| `seed` | Poista | Ei tuettu Responses API:ssa |

### O-sarja ennen/jälkeen

Ennen (Chat Completions o-sarjalla):
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

Jälkeen (Responses API):
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

> **Huom**: O-sarjan mallit voivat puskuroida tulostetta päättelyn aikana ennen tekstin deltojen lähettämistä. Suoratoisto toimii silti, mutta ensimmäinen `response.output_text.delta` -tapahtuma saattaa saapua pidemmällä viiveellä kuin GPT-malleissa.

## Päättelytokenien lukeminen
```python
# Päättelymallit käyttävät sisäistä päättelyä — voit nähdä, kuinka monta päättelytokenia käytettiin
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

> **Tärkeää**: Käytä `max_output_tokens=1000` (ei 50–200) päättelymallien sisäisen päättelyprosessin huomioimiseksi. Malli käyttää päättelytokenja sisäisesti ennen lopullisen tulosteen tuotantoa.

## Rakenteellinen tulos — JSON Schema
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

## Työkalujen käyttö

- Määrittele funktiot `tools`-kohdassa **tasaisessa Responses API -formaatissa** — `name`, `description` ja `parameters` ylimmällä tasolla (ei `function`-alle).
- Kun malli pyytää työkalun kutsua, suorita se sovelluksessasi ja liitä työkalun tulos seuraavaan pyyntöön `function_call_output`-kohteena `input`-sisällössä.
- Pidä skeemat minimissä; validoi syötteet ennen suoritusta.
- Käytettäessä `strict: true`, kaikkien ominaisuuksien pitää olla listattuna `required`-kentässä ja `additionalProperties: false` on pakollinen.

> **⚠️ `pydantic_function_tool()` on yhteensopimaton**: `openai.pydantic_function_tool()` -apuri tuottaa edelleen vanhan Chat Completions -sisäkkäisen muodon (`{"type": "function", "function": {"name": ...}}`). Älä käytä sitä `responses.create()` kanssa. Määrittele työkaluskeemat manuaalisesti tai kirjoita wrapper tasoittamaan ulostulo.

### Työkalun määrittelyformaatti

Responses API käyttää **tasoa** työkalumuotoa — `name`, `description`, `parameters` ovat ylimmän tason avaimia (eivät `function`-alle).

**Ennen (Chat Completions — sisäkkäinen):**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**Jälkeen (Responses API — tasainen):**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

Täysi esimerkki:
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

Käytettäessä `strict: true` (skeeman pakotus):
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
            "required": ["city_name"],       # Kaikkien ominaisuuksien TULEE olla listattuna
            "additionalProperties": False,   # Vaaditaan tiukkaa tilaa varten
        },
    }
]
```

### Työkalukutsun edestakainen käsittely (suorita ja palauta tulokset)

Kun malli pyytää työkalukutsua, käytä `response.output` -kohteita + `function_call_output` — **älä** käytä Chat Completionsin `role: assistant` + `role: tool` -mallia.

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
    # Lisää mallin function_call-kohteet keskusteluun
    messages.extend(response.output)

    # Suorita jokainen työkalu ja lisää tulokset
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # Hanki lopullinen vastaus työkalujen tulosten avulla
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot-työkalukutsuesimerkkejä

Kun annat few-shot-esimerkkejä työkalukutsuista `input`-kohdassa, käytä `function_call` ja `function_call_output` -kohteita. ID:t pitää alkaa `fc_`:llä.

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
# Sisäänrakennettu verkkohakuesimerkki
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Kuvan syöte

Kuvan sisältökohteiden tyyppi muuttuu `image_url` → `input_image`, ja URL vaihtelee sisäkkäisestä objektista tasaiseksi merkkijonoksi.

### Kuvan syöte — ennen (Chat Completions)
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

### Kuvan syöte — jälkeen (Responses API, URL)
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

### Kuvan syöte — jälkeen (Responses API, base64)
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

> **Keskeiset muutokset**: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}` (sisäkkäinen objekti) → `"image_url": "..."` (tasainen merkkijono — joko HTTPS-URL tai `data:image/...;base64,...` data URI), (3) `"type": "text"` → `"type": "input_text"`.

## Microsoft Agent Framework (MAF) siirtymä

**Tarkista ensin MAF-versiosi** — siirtymä riippuu siitä, oletko MAF 1.0.0+ vai versio ennen 1.0.0 beta/rc.

Tarkista: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+:ssa `OpenAIChatClient` **käyttää jo Responses APIa** — siirtymää ei tarvita.

Jos koodikanta käyttää vanhaa `OpenAIChatCompletionClient` (käyttää `chat.completions.create`), vaihda se `OpenAIChatClient`iin:

Ennen:
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

Jälkeen:
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

### MAF pre-1.0.0 (beta/rc julkaisut)

Pre-1.0.0 MAF:ssa `OpenAIChatClient` käytti Chat Completionsia. Päivitä `agent-framework-openai>=1.0.0` versioon, jossa `OpenAIChatClient` käyttää oletuksena Responses APIa.

> **Huom**: `Agent`, `MCPStreamableHTTPTool` ja muut MAF API:t pysyvät muuttumattomina — vain client-luokan import ja instansointi muuttuvat.

## LangChain (`langchain-openai`) siirtymä

Lisää `use_responses_api=True` `ChatOpenAI()`:iin. Päivitä myös viestien sisältöliittymä `.content` → `.text`.

Ennen:
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

# ... agentin kutsu ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

Jälkeen:
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

# ... agentin kutsu ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> **Keskeiset muutokset**: (1) `use_responses_api=True` konstruktorissa, (2) `.content` → `.text` vastauksissa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->