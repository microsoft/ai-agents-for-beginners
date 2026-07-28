# Testauksen infrastruktuurin migraatio

Siirrettäessä koodipohjaa Chat Completions -rajapinnasta Responses API:in, **testit rikkoutuvat ennustettavissa olevin tavoin**. Tämä viite kattaa, mitä korjata.

---

## Streaming-vastausten mokkaaminen (Python pytest)

### Keskeiset mokkausluokat

```python
class MockResponseEvent:
    """Simulates a Responses API streaming event."""
    def __init__(self, event_type: str, delta: str | None = None):
        self.type = event_type
        self.delta = delta

class AsyncResponseIterator:
    """Async iterator that yields Responses API streaming events from a string answer."""
    def __init__(self, answer: str):
        self.event_index = 0
        self.events = []
        for i, word in enumerate(answer.split(" ")):
            # Säilytä välilyönnit: lisää välilyönti kaikkien sanojen eteen paitsi ensimmäisen
            if i > 0:
                word = " " + word
            self.events.append(MockResponseEvent("response.output_text.delta", delta=word))
        self.events.append(MockResponseEvent("response.completed"))

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.event_index < len(self.events):
            event = self.events[self.event_index]
            self.event_index += 1
            return event
        raise StopAsyncIteration
```

### Vastausten reititys viestin sisällön mukaan

Aito sovellus tarjoaa eri vastauksia kehotteen mukaan. Reititä `input`-kentän perusteella (ei `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses-API käyttää 'input' ei 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch-polut

| Asiakas tyyppi | Monkeypatch-polku |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (synkroninen) | `openai.resources.responses.Responses.create` |

> **Ennen** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Jälkeen** (Responses): `openai.resources.responses.AsyncResponses.create`

### Täysi esimerkkifiksaattori

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... MockResponseEvent- ja AsyncResponseIterator-luokat tässä ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Päivitä mokkausfiksut

Vaihda `ChatCompletionChunk`-pohjaiset mokit edellä kuvattuun `MockResponseEvent` / `AsyncResponseIterator` -kuvioon. Keskeiset muutokset:

| Ennen (Chat Completions -moki) | Jälkeen (Responses-moki) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` palasessa | `event.type == "response.completed"` |
| Azure-spesifinen `prompt_filter_results` -pala | Poista kokonaan |
| Azure-spesifinen `content_filter_results` per valinta | Poista kokonaan |
| `kwargs.get("messages")` mokissa | `kwargs.get("input")` mokissa |

---

## 2. Päivitä snapshot- ja golden-tiedostot

Jos testipaketti käyttää snapshot-testausta (esim. `pytest-snapshot`, syrupy tai omatekoinen JSONL-snapshot), odotettu ulkonäkö muuttuu:

**Ennen** (Chat Completions streaming JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Jälkeen** (Responses API:n streaming JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Uusi rakenne on merkittävästi yksinkertaisempi — ei `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` tai `content_filter_results`-kenttiä. Päivitä tai regeneroi kaikki snapshot-tiedostot.

> **Vinkki**: Suorita testit `--snapshot-update`-lipulla (pytest-snapshot) tai `--update-snapshots`-lipulla (syrupy) migraation jälkeen automaattisesti uudelleenluodaksesi snapshotit.

---

## 3. Päivitä testien väitteet

Yleisiä väitevirheitä:

| Vanha väite | Ongelma | Uusi väite |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI`:lla ei ole `_azure_ad_token_provider`-attribuuttia | `isinstance(client, AsyncOpenAI)` ja `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Ei `api_version`-attribuuttia `OpenAI`/`AsyncOpenAI`-luokissa | Poista kokonaan |
| `isinstance(client, AsyncAzureOpenAI)` | Asiakastyyppi muuttui | `isinstance(client, AsyncOpenAI)` |

---

## 4. Päivitä ympäristömuuttujat testifiksuissa

Testit asettavat usein ympäristömuuttujia `monkeypatch.setenv`-menetelmällä. Päivitä nämä:

| Vanha ympäristömuuttuja | Uusi ympäristömuuttuja | Huomautukset |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Tavallinen Azure Identity SDK -käytäntö |
| `AZURE_OPENAI_VERSION` | Poista | Ei tarvetta `api_version`ille |
| `AZURE_OPENAI_API_VERSION` | Poista | Ei tarvetta `api_version`ille |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Säilytä (tarvitaan edelleen `base_url`iin) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Säilytä (deploy-nimi `model`-parametrille) |

---

## 5. Etsi siirtoa tarvitseva testikoodi

```bash
# Testikohtaiset perintökuviot
rg "ChatCompletionChunk" tests/
rg "AsyncCompletions\.create" tests/
rg "chat\.completions" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results" tests/
rg "content_filter_results" tests/
rg "AZURE_OPENAI_VERSION|AZURE_OPENAI_API_VERSION" tests/
rg "AZURE_OPENAI_CLIENT_ID" tests/
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->