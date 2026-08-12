# Миграција тест инфраструктуре

При миграцији кôд базе са Chat Completions на Responses API, **тестови се кваре на предвидљиве начине**. Ова референца обухвата шта треба исправити.

---

## Моковање стриминг одговора (Python pytest)

### Основне мок класе

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
            # Сачувај размаке: додај размак испред сваке речи осим прве
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

### Усмеравање мок одговора по садржају поруке

Праве апликације служе различите одговоре у зависности од упита. Усмери по `input` (а не `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API користи 'input', а не 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Путање за monkeypatch

| Тип клијента | Путања за monkeypatch |
|-------------|-----------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхронизовано) | `openai.resources.responses.Responses.create` |

> **Пре** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **После** (Responses): `openai.resources.responses.AsyncResponses.create`

### Целокупан пример fixture-а

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Овде се налазе класе MockResponseEvent и AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Ажурирајте mock fixture-ове

Замените мокове базиране на `ChatCompletionChunk` са горе поменутим обрасцем `MockResponseEvent` / `AsyncResponseIterator`. Кључне промене:

| Пре (Chat Completions мок) | После (Responses мок) |
|---------------------------|---------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` у чунку | `event.type == "response.completed"` |
| Azure специфичан `prompt_filter_results` чунк | Уклонити у потпуности |
| Azure специфичан `content_filter_results` по избору | Уклонити у потпуности |
| `kwargs.get("messages")` у mock-у | `kwargs.get("input")` у mock-у |

---

## 2. Ажурирајте snapshot / golden фајлове

Ако пакет тестова користи snapshot тестирање (нпр. `pytest-snapshot`, syrupy, или ручно рађене JSONL снимке), очекивани облик излаза се мења:

**Пре** (Chat Completions стриминг JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**После** (Responses API стриминг JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Нови облик је драстично једноставнији — без поља `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, или `content_filter_results`. Ажурирајте или регенеришите све snapshot фајлове.

> **Савет**: Покрените тестове са `--snapshot-update` (pytest-snapshot) или `--update-snapshots` (syrupy) након миграције да се аутоматски регенеришу.

---

## 3. Ажурирајте тестне претпоставке (assertions)

Уобичајене грешке у претпоставкама:

| Стари assertion | Проблем | Нови assertion |
|----------------|---------|----------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` нема атрибут `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` и `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Нема `api_version` на `OpenAI`/`AsyncOpenAI` | Уклонити у потпуности |
| `isinstance(client, AsyncAzureOpenAI)` | Тип клијента се променио | `isinstance(client, AsyncOpenAI)` |

---

## 4. Ажурирајте променљиве окружења у тест fixture-овима

Тестови често постављају environment variables преко `monkeypatch.setenv`. Ажурирајте их:

| Стари env var | Нови env var | Напомене |
|--------------|--------------|----------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандардна Azure Identity SDK конвенција |
| `AZURE_OPENAI_VERSION` | Уклонити | Није потребан `api_version` |
| `AZURE_OPENAI_API_VERSION` | Уклонити | Није потребан `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Оставити (још увек потребно за `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Оставити (име дистрибуције за параметар `model`) |

---

## 5. Потражите тест код који треба миграцију

```bash
# Наслеђени образци специфични за тестирање
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
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->