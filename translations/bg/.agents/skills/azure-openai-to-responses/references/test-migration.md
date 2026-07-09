# Миграция на тестовата инфраструктура

При мигриране на кодова база от Chat Completions към Responses API, **тестовете се чупят по предвидими начини**. Този референтен материал обхваща какво трябва да се поправи.

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
            # Запазете интервалите: добавете интервал пред всички думи, с изключение на първата
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

### Рутване на мок отговори според съдържанието на съобщението

Реалните приложения връщат различни отговори в зависимост от подсказката. Направете рутиране по `input` (не `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API за отговори използва 'input', а не 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Пътища за Monkeypatch

| Тип клиент | Път за Monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхронен) | `openai.resources.responses.Responses.create` |

> **Преди** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **След** (Responses): `openai.resources.responses.AsyncResponses.create`

### Пълен пример на фикстура

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Класове MockResponseEvent и AsyncResponseIterator тук ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Актуализирайте мок фикстурите

Заменете моковете на базата на `ChatCompletionChunk` с горния модел `MockResponseEvent` / `AsyncResponseIterator`. Ключови промени:

| Преди (Chat Completions мок) | След (Responses мок) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` в чънка | `event.type == "response.completed"` |
| Специфичен за Azure чънк `prompt_filter_results` | Премахнете напълно |
| Специфични за Azure `content_filter_results` на избор | Премахнете напълно |
| `kwargs.get("messages")` в мок | `kwargs.get("input")` в мок |

---

## 2. Актуализирайте snapshot / golden файловете

Ако тестовият комплект използва snapshot тестване (например `pytest-snapshot`, syrupy или ръчно направени JSONL snapshot-и), очакваната форма на изхода се променя:

**Преди** (чат комплишъни стрийминг JSONL):
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

Новата форма е значително по-проста — няма полета `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` или `content_filter_results`. Актуализирайте или регенерирайте всички snapshot файлове.

> **Съвет**: Изпълнете тестовете с `--snapshot-update` (pytest-snapshot) или `--update-snapshots` (syrupy) след миграцията, за да се регенерират автоматично.

---

## 3. Актуализирайте тестовите твърдения

Чести счупвания на твърдения:

| Старо твърдение | Проблем | Ново твърдение |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` няма атрибут `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` и `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Няма `api_version` на `OpenAI`/`AsyncOpenAI` | Махнете напълно |
| `isinstance(client, AsyncAzureOpenAI)` | Типът клиент се е променил | `isinstance(client, AsyncOpenAI)` |

---

## 4. Актуализирайте променливите на средата в тестовите фикстури

Тестовете често задават променливи на средата чрез `monkeypatch.setenv`. Актуализирайте ги:

| Стара пр. на средата | Нова пр. на средата | Забележки |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандартната конвенция на Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Премахнете | Не е нужно `api_version` |
| `AZURE_OPENAI_API_VERSION` | Премахнете | Не е нужно `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Запазете (все още е нужна за `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Запазете (име на деплой за параметъра `model`) |

---

## 5. Потърсете тестов код, който се нуждае от миграция

```bash
# Тестово специфични наследени модели
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