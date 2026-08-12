# 測試基礎設施遷移

在將程式碼庫從 Chat Completions 遷移到 Responses API 時，<strong>測試會以可預測的方式失效</strong>。此參考涵蓋需要修復的內容。

---

## 模擬串流回應 (Python pytest)

### 核心模擬類別

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
            # 保留空白：在除第一個字之外的所有詞前加空格
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

### 根據訊息內容路由模擬回應

實際應用程式會根據提示提供不同答案。請依 `input` 路由（非 `messages`）：

```python
async def mock_acreate(*args, **kwargs):
    # 回應 API 使用 'input' 而非 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch 路徑

| 客戶端類型 | Monkeypatch 路徑 |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (同步) | `openai.resources.responses.Responses.create` |

> <strong>之前</strong>（Chat Completions）：`openai.resources.chat.AsyncCompletions.create`
> <strong>之後</strong>（Responses）：`openai.resources.responses.AsyncResponses.create`

### 完整的測試夾具範例

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... 這裡是 MockResponseEvent 和 AsyncResponseIterator 類別 ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. 更新模擬測試夾具

將基於 `ChatCompletionChunk` 的模擬替換為上述的 `MockResponseEvent` / `AsyncResponseIterator` 模式。主要改動：

| 之前（Chat Completions 模擬） | 之後（Responses 模擬） |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| chunk 中的 `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure 專用的 `prompt_filter_results` chunk | 完全移除 |
| Azure 專用的每個選項的 `content_filter_results` | 完全移除 |
| 模擬中的 `kwargs.get("messages")` | 模擬中的 `kwargs.get("input")` |

---

## 2. 更新快照 / 金色檔案

如果測試套件使用快照測試（例如，`pytest-snapshot`、syrupy，或自行實作的 JSONL 快照），預期輸出格式會更改：

<strong>之前</strong>（Chat Completions 串流 JSONL）：
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

<strong>之後</strong>（Responses API 串流 JSONL）：
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

新格式明顯簡化 — 不再有 `function_call`、`refusal`、`role`、`tool_calls`、`index`、`logprobs` 或 `content_filter_results` 欄位。請更新或重新產生所有快照檔案。

> <strong>提示</strong>：遷移後，使用 `--snapshot-update`（pytest-snapshot）或 `--update-snapshots`（syrupy）執行測試以自動重新產生快照。

---

## 3. 更新測試斷言

常見斷言失效情況：

| 舊斷言 | 問題 | 新斷言 |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` 沒有 `_azure_ad_token_provider` 屬性 | `isinstance(client, AsyncOpenAI)` 且 `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` 無 `api_version` 屬性 | 完全移除 |
| `isinstance(client, AsyncAzureOpenAI)` | 客戶端類型已變更 | `isinstance(client, AsyncOpenAI)` |

---

## 4. 更新測試夾具中的環境變數

測試中常用 `monkeypatch.setenv` 設定環境變數。請更新為：

| 舊環境變數 | 新環境變數 | 備註 |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | 標準 Azure 身份驗證 SDK 慣例 |
| `AZURE_OPENAI_VERSION` | 移除 | 不再需要 `api_version` |
| `AZURE_OPENAI_API_VERSION` | 移除 | 不再需要 `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | 保留（仍用於 `base_url`） |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | 保留（用於 `model` 參數的部署名稱） |

---

## 5. 搜尋需要遷移的測試程式碼

```bash
# 測試專用的舊有模式
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
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->