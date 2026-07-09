# Міграція тестової інфраструктури

Під час міграції кодової бази з Chat Completions на Responses API **тести ламаються передбачуваними способами**. Це довідкове керівництво пояснює, що виправити.

---

## Імітація потокових відповідей (Python pytest)

### Основні класи-заглушки

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
            # Зберегти пропуски: додати пробіл перед усіма словами, окрім першого
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

### Маршрутизація відповідей-заглушок за вмістом повідомлення

Реальні додатки повертають різні відповіді залежно від запиту. Маршрутизувати за `input` (не за `messages`):

```python
async def mock_acreate(*args, **kwargs):
    # API відповідей використовує 'input', а не 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Шляхи для Monkeypatch

| Тип клієнта | Шлях для monkeypatch |
|-------------|---------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхронний) | `openai.resources.responses.Responses.create` |

> **Раніше** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Тепер** (Responses): `openai.resources.responses.AsyncResponses.create`

### Повний приклад fixture

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Тут класи MockResponseEvent та AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Оновіть mock fixtures

Замініть заглушки на основі `ChatCompletionChunk` патерном `MockResponseEvent` / `AsyncResponseIterator`, наведеним вище. Основні зміни:

| Раніше (mock Chat Completions) | Тепер (mock Responses) |
|-------------------------------|----------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` у чанку | `event.type == "response.completed"` |
| Чанк `prompt_filter_results`, специфічний для Azure | Видалити повністю |
| `content_filter_results` на вибір, специфічний для Azure | Видалити повністю |
| `kwargs.get("messages")` у mock | `kwargs.get("input")` у mock |

---

## 2. Оновіть snapshot / golden файли

Якщо тестовий набір використовує тестування за знімками (наприклад, `pytest-snapshot`, syrupy або власноруч створені JSONL-знімки), змінюється очікувана структура вихідних даних:

**Раніше** (потоковий Chat Completions JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Тепер** (потоковий Responses API JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Нова структура набагато простіша — немає полів `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` або `content_filter_results`. Оновіть або перегенеруйте всі файли знімків.

> **Порада**: Запускайте тести з `--snapshot-update` (pytest-snapshot) або `--update-snapshots` (syrupy) після міграції для автоматичного перегенерування.

---

## 3. Оновіть твердження у тестах

Найпоширеніші зломи тверджень:

| Старе твердження | Проблема | Нове твердження |
|-----------------|----------|------------------|
| `client._azure_ad_token_provider is not None` | У `AsyncOpenAI` немає атрибуту `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` і `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Немає `api_version` у `OpenAI`/`AsyncOpenAI` | Видалити повністю |
| `isinstance(client, AsyncAzureOpenAI)` | Змінився тип клієнта | `isinstance(client, AsyncOpenAI)` |

---

## 4. Оновіть змінні оточення у тестових fixture

Тести часто встановлюють змінні оточення через `monkeypatch.setenv`. Оновіть їх так:

| Стара змінна оточення | Нова змінна оточення | Примітки |
|-----------------------|----------------------|----------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандартна конвенція Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Видалити | `api_version` не потрібен |
| `AZURE_OPENAI_API_VERSION` | Видалити | `api_version` не потрібен |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Залишити (все ще потрібен для `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Залишити (ім'я розгортання для параметра `model`) |

---

## 5. Знайдіть код тестів, який потребує міграції

```bash
# Спадкові шаблони, специфічні для тесту
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
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->