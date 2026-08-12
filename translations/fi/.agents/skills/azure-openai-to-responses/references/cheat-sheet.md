# Responses API Pikakertaus (Python + Azure OpenAI)

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

## Clientin asetukset — EntraID (suositeltu)
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

## Clientin asetukset — API-avain
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## Async clientin asetukset — EntraID
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

## Async clientin asetukset — EntraID eksplisiittisellä tenantilla (monivuokraaja)

Kun Azure OpenAI -resurssi on **eri tenantissa** kuin oletus, anna `tenant_id` eksplisiittisesti tunnistetietoon. Tämä on yleistä kehitys/testaus-ympäristöissä, joissa kehittäjän kotitenantti poikkeaa resurssin tenantista.

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# ManagedIdentityCredential tuotantoon (Azure Container Apps, App Service, jne.)
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # käyttäjän määrittämä hallittu identiteetti
)
# AzureDeveloperCliCredential paikalliseen kehitykseen — eksplisiittinen tenant_id on olennainen
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# Ketju: kokeile ensin hallittua identiteettiä, palaa azd CLI:hin tarvittaessa
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
    model="gpt-4.1",
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

## Täysi synkroninen siirtymä — ennen/jälkeen

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
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

Jälkeen (Responses API — Azure OpenAI v1-päätepiste):
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

## Suoratoisto (synkronoitu)
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

## Suoratoisto (asynkronoitu)
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

## Web-sovelluksen suoratoisto — tausta-frontend -muoto

Kun siirrät web-sovellusta, joka suoratoistaa SSE/JSONL-viestejä frontendille, **taustan sarjoitusmuoto** muuttuu. Suunnittele uusi taustan tulostus säilyttämään frontendin olemassa olevat käyttökuviot, jotta frontend ei tarvitse muutoksia.

**Ennen** — Chat Completions -tausta sarjoitti tyypillisesti jokaisen palan `choices[0]` sanakirjan:
```python
# Vanha: sarjallistettu täydellinen valintasanakirja per lohko
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
Frontend lukee: `response.delta.content` (syvä polku valintaobjektiin).

**Jälkeen** — Responses API -tausta tuottaa minimaalisen rakenteen, joka säilyttää saman frontendin käyttöpolun:
```python
# Uusi: lähetä vain se, mitä frontend tarvitsee
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
Frontend lukee edelleen `response.delta.content` — **frontend ei tarvitse muutoksia**.

> **Keskeinen oivallus**: Responses API:n suoratoiston rakenne (`event.type` + `event.delta`) on periaatteessa erilainen kuin Chat Completions (`chunk.choices[0].delta.content`). Mutta sinun tausta-frontend -sopimus on sinun määriteltävä. Muotoile taustan tulostus vastaamaan sitä, mitä frontend jo odottaa.

## Suoratoiston tapahtumasarja

Kun `stream: true`, API lähettää tapahtumat tässä järjestyksessä:
1. `response.created` – vastausobjekti alustettu
2. `response.in_progress` – generointi aloitettu
3. `response.output_item.added` – tulosteen osa luotu
4. `response.content_part.added` – sisällön osa aloitettu
5. `response.output_text.delta` – tekstipalat (useita, jokaisella on `delta: string`)
6. `response.output_text.done` – tekstin generointi valmis
7. `response.content_part.done` – sisällön osa valmis
8. `response.output_item.done` – tulosteosa valmis
9. `response.completed` – koko vastaus valmis

Perustekstisuoratoistossa käsittele vain `response.output_text.delta` (tekstipalojen käsittelyyn) ja `response.completed` (valmiin merkitsemiseen).

## Suoratoiston virheenkäsittely web-sovelluksissa

Kun suoratoistat web-sovelluksessa, kiedo asynkroninen iteraatio `try/except`-lohkoon ja lähetä virheet JSON-muodossa, jotta frontend voi näyttää ne siististi (esim. nopeusrajoitukset, tilapäiset virheet):

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

> **Miksi tämä on tärkeää**: Azure OpenAI palauttaa `429 Too Many Requests` nopeusrajoituksen aikana. Ilman `try/except`-lohkoa suoratoisto keskeytyy hiljaa. Lohkon kanssa frontend saa `{"error": "Too Many Requests"}` ja voi näyttää uudelleenyrityskehotuksen.

## Suoratoiston tapahtumatyyppit (Python SDK)

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## Keskustelun muoto
```python
# Vastausrajapinta tukee keskustelumuotoa syöte-taulukon avulla
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

## Sisällön suodattimen virheenkäsittely

Virhersturktuuuri muuttui Chat Completionsista Responses API:in.

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
- `innererror`-kääre on **poistettu** — sisällön suodattimen tiedot ovat nyt `error.body`:n päällä.
- `content_filter_result` (yksikkö) → `content_filters` (monikko-taulukko), joka sisältää `content_filter_results` (monikko) jokaisessa merkinnässä.
- Jokainen merkintä `content_filters` sisältää `blocked`, `source_type` ja `content_filter_results` kategoriakohtaisine tietoineen (`jailbreak`, `hate`, `sexual`, `violence`, `self_harm`).

Täysi Responses API:n sisällönsuodattimen virheen runkorakenne:
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

Jos sovellus kutsuu Azure OpenAI REST:iä suoraan ilman SDK:ta:

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

> **Huom:** `output_text` on Python SDK:n `Response`-objektin kätevä attribuutti. Raaka REST JSON -vastaus ei sisällä päällimmäistä `output_text`-kenttää — teksti on kohdassa `output[0].content[0].text`.

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

Sisällön tyypitetyssä monikierroksisessa (eksplisiittinen `input_text`/`output_text`):
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### Monikierros `previous_response_id` avulla (vaihtoehto)

Sen sijaan, että hallinnoisit keskustelua taulukossa itse, voit ketjuttaa vastauksia
palvelinpuolella käyttämällä `previous_response_id`:tä. API tallentaa jokaisen vastauksen ja
lisää automaattisesti aiemmat vuorot eteen.

```python
# Ensimmäinen vuoro
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# Seuraavat vuorot — lähetä vain uusi käyttäjän viesti + edellisen vastauksen tunniste
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**Milloin käyttää kumpaa:**

| Lähestymistapa | Hyödyt | Haitat |
|---|---|---|
| `input`-taulukko (manuaalinen) | Täysi hallinta historiasta; voi rajata/tiivistää; ei tarvetta palvelinpuolen tallennukselle (`store=False`) | Lisää koodia; hallinnoit taulukkoa itse |
| `previous_response_id` | Yksinkertaisempi koodi; automaattinen ketjutus | Vaatii `store=True` (oletus); keskustelu tallennetaan palvelimelle; ei voi muokata historiaa vuorojen välillä |

> **Siirtymismuistutus:** Useimmat Chat Completions -sovellukset hallinnoivat jo viestitaulukkoa itse, joten `input`-taulukkoon siirtyminen on suoraviivainen 1:1-muutos. Käytä `previous_response_id`:tä uudessa koodissa tai kun et tarvitse keskusteluhistorian muokkausta.

## O-sarjan päättelymallit (o1, o3-mini, o3, o4-mini)

O-sarjan malleilla on erityisiä parametrirajoituksia siirryttäessä Responses API:iin.

### Parametrien kartoitus o-sarjalle

| Chat Completions (o-sarja) | Responses API | Huomautuksia |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | Aseta korkea arvo (4096+) — päättelytokenit lasketaan rajoitukseen |
| `reasoning_effort` | `reasoning.effort` | Säilytä ennallaan, jos on (low/medium/high) |
| `temperature` | Poista tai aseta `1` | O-sarja hyväksyy vain `1` |
| `top_p` | Poista | Ei tuettu o-sarjalla |
| `seed` | Poista | Ei tuettu Responses API:ssa |

### O-sarjan ennen/jälkeen

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

> **Huom**: O-sarjan mallit voivat puskuroida tulosta päättelyn aikana ennen tekstideltan lähettämistä. Suoratoisto toimii silti, mutta ensimmäinen `response.output_text.delta` voi saapua pidemmän viiveen jälkeen verrattuna GPT-malleihin.

## Pääsy päättelytokeneihin
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

> **Tärkeää**: Käytä `max_output_tokens=1000` (ei 50–200) ottaaksesi huomioon päättelymallien sisäisen päättelyn. Malli käyttää päättelytokeneita sisäisesti ennen lopullisen tulosteen generointia.

## Rakenteinen tuloste — JSON Schema
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

## Työkalun käyttö

- Määrittele funktiot `tools`-kentässä käyttäen **tasainen Responses API -formaatti** — `name`, `description` ja `parameters` ovat päällimmäisellä tasolla (ei `function`-avaimen alla).
- Kun malli pyytää työkalun kutsua, suorita se sovelluksessasi ja sisällytä työkalun tulos seuraavaan pyyntöön `function_call_output`-kohteena `input`-sisällä.
- Pidä skeemat minimalistisina; validoi syötteet ennen suoritusta.
- Kun käytät `strict: true` -asetusta, kaikki ominaisuudet on listattava `required`-kohdassa ja `additionalProperties: false` on pakollinen.

> **⚠️ `pydantic_function_tool()` ei ole yhteensopiva**: `openai.pydantic_function_tool()`-avustaja tuottaa edelleen vanhan Chat Completions -rakenteen (`{"type": "function", "function": {"name": ...}}`). Älä käytä sitä `responses.create()` kanssa. Määrittele työkaluskeemat manuaalisesti tai kirjoita wrapper tekemään output litteäksi.

### Työkalun määrittelyformaatti

Responses API käyttää **tasapintaista** työkalumuotoa — `name`, `description`, `parameters` ovat ylimmällä tasolla (ei `function`-avaimen alla).

**Ennen (Chat Completions — sisäinen):**
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

Kun käytössä `strict: true` (skeeman noudattaminen):
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
            "required": ["city_name"],       # Kaikki ominaisuudet TULEE luetella
            "additionalProperties": False,   # Pakollinen tiukkaa tilaa varten
        },
    }
]
```

### Työkalun kutsun kahdensuuntainen käsittely (suorita ja palauta tulokset)

Kun malli pyytää työkalun kutsua, käytä `response.output`-kohteita + `function_call_output` — **ei** Chat Completions -mallin `role: assistant` + `role: tool` -kuviota.

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

    # Hanki lopullinen vastaus työkalujen tuloksilla
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Harjoitustyökalun kutsuesimerkit

Kun annat harjoitusesimerkkejä työkalukutsuista `input`-kentässä, käytä `function_call` ja `function_call_output`-kohteita. ID:t pitää alkaa `fc_`:llä.

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
# Sisäänrakennetun verkkohakutoiminnon esimerkki
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## Kuvan syöttö

Kuvan sisältömuutokset muuttavat tyypin `image_url`:stä `input_image`:ksi, ja URL muuttuu sisäkkäisestä objektista tasaiseksi merkkijonoksi.

### Kuvan syöttö — ennen (Chat Completions)
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

### Kuvan syöttö — jälkeen (Responses API, URL)
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

### Kuvan syöttö — jälkeen (Responses API, base64)
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

## Microsoft Agent Framework (MAF) -siirtymä

**Tarkista ensin MAF-versiosi** — siirtymä riippuu siitä, oletko MAF 1.0.0+ vai pre-1.0.0 beta/rc.

Tarkistus: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+:ssa `OpenAIChatClient` **käyttää jo Responses API:a** — siirtymää ei tarvita.

Jos koodikanta käyttää vanhaa `OpenAIChatCompletionClient` (käyttää `chat.completions.create`), vaihda se `OpenAIChatClient`:iin:

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

Pre-1.0.0 MAF:ssa `OpenAIChatClient` käytti Chat Completionsia. Päivitä `agent-framework-openai>=1.0.0` versioon, jossa `OpenAIChatClient` käyttää oletuksena Responses API:a.

> **Huom:** `Agent`, `MCPStreamableHTTPTool` ja muut MAF API:t pysyvät muuttumattomina — ainoastaan client-luokan tuonti ja luonti muuttuvat.

## LangChain (`langchain-openai`) siirtymä

Lisää `use_responses_api=True` `ChatOpenAI()` konstruktorin argumentteihin. Päivitä myös viestien sisältösyöttö `.content` → `.text`.

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

> **Keskeiset muutokset**: (1) `use_responses_api=True` konstruktorissa, (2) `.content` → `.text` vastausviesteissä.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->