# Миграција тест инфраструктуре

Када се врши миграција код базе са Chat Completions на Responses API, **тестови се кваре на предвидиве начине**. Овај референтни водич обухвата шта је потребно исправити.

---

## Моковање стримовања одговора (Python pytest)

### Кључне mock класе

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
            # Задржи размак: додај размак испред сваке речи осим прве
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

### Рутирање mock одговора по садржају поруке

Праве апликације служе различите одговоре у зависности од упита. Руттирај по `input` (не по `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API за одговоре користи 'input' а не 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Путање за монкипатрч

| Тип клијента | Путиња монкипатча |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхрони) | `openai.resources.responses.Responses.create` |

> **Пре** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **После** (Responses): `openai.resources.responses.AsyncResponses.create`

### Целокупан пример фикстуре

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Класе MockResponseEvent и AsyncResponseIterator овде ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Ажурирај mock фикстуре

Замени `ChatCompletionChunk`-базиране mock-ове са `MockResponseEvent` / `AsyncResponseIterator` патерном изнад. Кључне промене:

| Пре (Chat Completions mock) | После (Responses mock) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` у исечку | `event.type == "response.completed"` |
| Azure-специфични `prompt_filter_results` исечак | Уклони у потпуности |
| Azure-специфични `content_filter_results` по избору | Уклони у потпуности |
| `kwargs.get("messages")` у mock-у | `kwargs.get("input")` у mock-у |

---

## 2. Ажурирај снимке / golden фајлове

Ако тест скуп користи snapshot тестирање (нпр. `pytest-snapshot`, syrupy, или ручно рађене JSONL снимке), очекивани облик излаза се мења:

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

Нови облик је драстично једноставнији — нема поља `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs`, или `content_filter_results`. Ажурирај или регенериши све снимке.

> **Савет**: Покрени тестове са `--snapshot-update` (pytest-snapshot) или `--update-snapshots` (syrupy) након миграције да се аутоматски регенеришу.

---

## 3. Ажурирај тврдње у тестовима

Уобичајени кварови у тврдњама:

| Стари услов | Проблем | Нови услов |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` нема атрибут `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` и `"/openai/v1/" у стр(client.base_url)` |
| `client.api_version == "2024-..."` | Нема `api_version` у `OpenAI`/`AsyncOpenAI` | Уклони у потпуности |
| `isinstance(client, AsyncAzureOpenAI)` | Тип клијента је промењен | `isinstance(client, AsyncOpenAI)` |

---

## 4. Ажурирај променљиве окружења у тест фикстурама

Тестови често подешавају env vars преко `monkeypatch.setenv`. Ажурирај ове:

| Стари env var | Нови env var | Напомене |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандардна конвенција Azure Identity SDK-а |
| `AZURE_OPENAI_VERSION` | Уклони | Нема потребе за `api_version` |
| `AZURE_OPENAI_API_VERSION` | Уклони | Нема потребе за `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Остани (још увек потребно за `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Остани (име деплоја за `model` параметар) |

---

## 5. Потражи тест код који треба миграцију

```bash
# Остављени шаблони специфични за тест
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