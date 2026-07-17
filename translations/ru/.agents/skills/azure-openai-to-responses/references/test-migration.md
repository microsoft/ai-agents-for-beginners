# Миграция тестовой инфраструктуры

При миграции кода с Chat Completions на Responses API **тесты ломаются предсказуемым образом**. В этом справочнике описано, что нужно исправить.

---

## Мокирование потоковых ответов (Python pytest)

### Базовые классы моков

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
            # Сохраняйте пробелы: добавляйте пробел перед всеми словами, кроме первого
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

### Маршрутизация мок-ответов по содержимому сообщения

Реальные приложения возвращают разные ответы в зависимости от запроса. Маршрутизируйте по `input` (а не по `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # Responses API использует 'input', а не 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Пути для monkeypatch

| Тип клиента | Путь для monkeypatch |
|-------------|---------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхронный) | `openai.resources.responses.Responses.create` |

> **Ранее** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Теперь** (Responses): `openai.resources.responses.AsyncResponses.create`

### Полный пример фикстуры

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Классы MockResponseEvent и AsyncResponseIterator здесь ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Обновите мок-фикстуры

Замените моки на основе `ChatCompletionChunk` на паттерн с `MockResponseEvent` / `AsyncResponseIterator`, как показано выше. Основные изменения:

| Ранее (мок Chat Completions) | Теперь (мок Responses) |
|------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` в чанке | `event.type == "response.completed"` |
| Специфичный для Azure чанк `prompt_filter_results` | Удалить полностью |
| Специфичный для Azure `content_filter_results` на выбор | Удалить полностью |
| В моках `kwargs.get("messages")` | В моках `kwargs.get("input")` |

---

## 2. Обновите снэпшоты / золотые файлы

Если в тестах используется снэпшот-тестирование (например, `pytest-snapshot`, syrupy или самописные JSONL-снэпшоты), ожидаемая структура вывода изменяется:

**Ранее** (Chat Completions потоковый JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Теперь** (Responses API потоковый JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Новая структура значительно проще — без полей `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` или `content_filter_results`. Обновите или пересоздайте все файлы снэпшотов.

> **Совет**: Запускайте тесты с `--snapshot-update` (pytest-snapshot) или `--update-snapshots` (syrupy) после миграции, чтобы автоматически обновить снэпшоты.

---

## 3. Обновите утверждения в тестах

Распространённые поломки утверждений:

| Старое утверждение | Проблема | Новое утверждение |
|-------------------|----------|-------------------|
| `client._azure_ad_token_provider is not None` | В `AsyncOpenAI` нет атрибута `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` и `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Нет `api_version` у `OpenAI`/`AsyncOpenAI` | Удалить полностью |
| `isinstance(client, AsyncAzureOpenAI)` | Тип клиента изменён | `isinstance(client, AsyncOpenAI)` |

---

## 4. Обновите переменные окружения в тестовых фикстурах

Тесты часто устанавливают env vars через `monkeypatch.setenv`. Обновите их:

| Старая переменная окружения | Новая переменная окружения | Примечания |
|----------------------------|----------------------------|-----------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандартное соглашение Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Удалить | `api_version` больше не нужен |
| `AZURE_OPENAI_API_VERSION` | Удалить | `api_version` больше не нужен |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Оставить (по-прежнему нужен для `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Оставить (имя деплоймента для параметра `model`) |

---

## 5. Поиск тестового кода, требующего миграции

```bash
# Специфичные для теста устаревшие шаблоны
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
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->