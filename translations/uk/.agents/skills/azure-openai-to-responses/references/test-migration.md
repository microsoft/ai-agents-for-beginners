# Міграція інфраструктури тестування

Під час міграції коду з Chat Completions на Responses API **тести ламаються передбачуваними способами**. Це довідник, що пояснює, що потрібно виправити.

---

## Мокінг потокових відповідей (Python pytest)

### Основні мок-класи

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
            # Зберегти пробіли: додати пропуск перед усіма словами, крім першого
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

### Маршрутизація мок-відповідей за вмістом повідомлення

Реальні застосунки надають різні відповіді залежно від запиту. Маршрутизувати за `input` (не `messages`):

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

### Шляхи для monkeypatch

| Тип клієнта | Шлях monkeypatch |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (синхронний) | `openai.resources.responses.Responses.create` |

> **Раніше** (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> **Після** (Responses): `openai.resources.responses.AsyncResponses.create`

### Повний приклад фікстури

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... Тут класи MockResponseEvent і AsyncResponseIterator ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. Оновити мок-фікстури

Замініть моки на основі `ChatCompletionChunk` на патерн `MockResponseEvent` / `AsyncResponseIterator`, як описано вище. Основні зміни:

| Раніше (мок Chat Completions) | Тепер (мок Responses) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| `finish_reason="stop"` в чанку | `event.type == "response.completed"` |
| Azure-специфічний чан `prompt_filter_results` | Видалити повністю |
| Azure-специфічний `content_filter_results` для кожного вибору | Видалити повністю |
| `kwargs.get("messages")` в моках | `kwargs.get("input")` в моках |

---

## 2. Оновлення snapshot / golden файлів

Якщо тестовий набір використовує snapshot тестування (наприклад, `pytest-snapshot`, syrupy або власні JSONL snapshot-и), форма очікуваного результату змінюється:

**Раніше** (Chat Completions потоковий JSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

**Після** (Responses API потоковий JSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

Нова форма значно простіша — без полів `function_call`, `refusal`, `role`, `tool_calls`, `index`, `logprobs` чи `content_filter_results`. Оновіть або перегенеруйте всі snapshot файли.

> **Порада**: Запускайте тести з `--snapshot-update` (pytest-snapshot) або `--update-snapshots` (syrupy) після міграції для автоматичного оновлення.

---

## 3. Оновлення тестових тверджень

Часті проблеми з твердженнями:

| Старе твердження | Проблема | Нове твердження |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` не має атрибуту `_azure_ad_token_provider` | `isinstance(client, AsyncOpenAI)` та `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | Немає `api_version` у `OpenAI`/`AsyncOpenAI` | Видалити повністю |
| `isinstance(client, AsyncAzureOpenAI)` | Тип клієнта змінився | `isinstance(client, AsyncOpenAI)` |

---

## 4. Оновлення змінних середовища у тестових фікстурах

Тести часто встановлюють змінні середовища через `monkeypatch.setenv`. Оновіть їх:

| Стара змінна середовища | Нова змінна середовища | Примітки |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | Стандартна конвенція Azure Identity SDK |
| `AZURE_OPENAI_VERSION` | Видалити | Не потрібен `api_version` |
| `AZURE_OPENAI_API_VERSION` | Видалити | Не потрібен `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | Залишити (причина для `base_url`) |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | Залишити (назва розгортання для параметра `model`) |

---

## 5. Пошук коду тестів, який потребує міграції

```bash
# Специфічні для тесту спадкові шаблони
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