# Миграция на тестова инфраструктура

При миграция на кодова база от Chat Completions към Responses API, **тестовете се чупят по предсказуеми начини**. Този референтен материал обяснява какво трябва да се поправи.

---

## Мокиране на стрийминг отговори (Python pytest)

### Основни мок класове

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
            # Запази интервалите: добави интервал пред всички думи, освен първата
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

### Маршрутизиране на мок отговори според съдържанието на съобщението

Реалните приложения предоставят различни отговори според промпта. Маршрутизирайте по `input` (не по `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API за отговори използва 'input', не 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Пътища за monkeypatch

| Тип клиент | Път за monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхронен) | `openai.resources.responses.Responses.create` |

> **Преди** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **След** (Responses): `openai.resources.responses.AsyncResponses.create`

### Пълен пример за фикстура

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... тук са класовете MockResponseEvent и AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Обновете мок фикстурите

Заменете моковете, базирани на `ChatCompletionChunk`, с горния модел `MockResponseEvent` / `AsyncResponseIterator`. Ключови промени:

| Преди (mock за Chat Completions) | След (mock за Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` в chunk | `event.type == "response.completed"` |
| Azure-специфичен chunk `prompt_filter_results` | Изцяло премахнете |
| Azure-специфичен `content_filter_results` за избор | Изцяло премахнете |
| `kwargs.get("messages")` в mock | `kwargs.get("input")` в mock |

---

## 2. Обновете snapshot / golden файловете

Ако тестовият пакет използва snapshot тестване (напр. `pytest-snapshot`, syrupy или ръчно направени JSONL snapshots), очакваната форма на изхода се променя:

**Преди** (Chat Completions стрийминг JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**След** (Responses API стрийминг JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Новата форма е значително по-проста — без полетата `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` или `content_filter_results`. Обновете или регенерирайте всички snapshot файлове.

> **Подсказка**: Стартирайте тестовете с `--snapshot-update` (pytest-snapshot) или `--update-snapshots` (syrupy) след миграцията за автоматично регенериране.

---

## 3. Обновете тестовите асерции

Чести счупвания на асерции:

| Стара асерция | Проблем | Нова асерция |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` няма атрибут `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` и `"/openai/v1/" в str(client.base_url)` |
| `client.api_version == "2024-..."` | Няма `api_version` в `OpenAI`/`AsyncOpenAI` | Премахнете изцяло |
| `isinstance(client, AsyncAzureOpenAI)` | Типът клиент се е променил | `isinstance(client, AsyncOpenAI)` |

---

## 4. Обновете променливите на околната среда в тестови фикстури

Тестовете често задават env vars чрез `monkeypatch.setenv`. Обновете ги:

| Стара env var | Нова env var | Бележки |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандартна конвенция на Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Премахнете | Не е нужна `api_version` |
| `AZURE_OPENAI_API_VERSION` | Премахнете | Не е нужна `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Запазете (все още необходим за `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Запазете (име на деплоймънт за параметър `model`) |

---

## 5. Потърсете тестов код, който трябва да бъде мигриран

```bash
# Наследени шаблони, специфични за теста
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
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->