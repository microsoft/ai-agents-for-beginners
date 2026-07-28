# 测试基础设施迁移

当将代码库从 Chat Completions 迁移到 Responses API 时，<strong>测试会以可预测的方式失败</strong>。本参考资料涵盖了需要修复的内容。

---

## 模拟流式响应（Python pytest）

### 核心模拟类

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
            # 保留空白：除了第一个单词外，在所有单词前加空格
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

### 按消息内容路由模拟响应

真实应用根据提示提供不同的答案。按 `input` 路由（不是 `messages`）：

```python
async def mock_acreate(*args, **kwargs):
    # 响应 API 使用 'input' 而不是 'messages'
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch 路径

| 客户端类型 | Monkeypatch 路径 |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI`（同步） | `openai.resources.responses.Responses.create` |

> <strong>之前</strong>（Chat Completions）：`openai.resources.chat.AsyncCompletions.create`
> <strong>之后</strong>（Responses）：`openai.resources.responses.AsyncResponses.create`

### 完整示例夹具

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... 这里是 MockResponseEvent 和 AsyncResponseIterator 类 ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. 更新模拟夹具

用上面的 `MockResponseEvent` / `AsyncResponseIterator` 模式替换基于 `ChatCompletionChunk` 的模拟。主要变化：

| 之前（Chat Completions 模拟） | 之后（Responses 模拟） |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| 分块中的 `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure 特定的 `prompt_filter_results` 分块 | 完全移除 |
| 每个选项的 Azure 特定 `content_filter_results` | 完全移除 |
| 模拟中的 `kwargs.get("messages")` | 模拟中的 `kwargs.get("input")` |

---

## 2. 更新快照 / 金色文件

如果测试套件使用快照测试（例如 `pytest-snapshot`、syrupy，或自制的 JSONL 快照），预期输出结构发生变化：

<strong>之前</strong>（Chat Completions 流式 JSONL）：
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

<strong>之后</strong>（Responses API 流式 JSONL）：
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

新的结构大幅简化 —— 无 `function_call`、`refusal`、`role`、`tool_calls`、`index`、`logprobs` 或 `content_filter_results` 字段。更新或重新生成所有快照文件。

> <strong>提示</strong>：迁移后使用 `--snapshot-update`（pytest-snapshot）或 `--update-snapshots`（syrupy）运行测试以自动重新生成。

---

## 3. 更新测试断言

常见断言失败：

| 旧断言 | 问题 | 新断言 |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` 没有 `_azure_ad_token_provider` 属性 | `isinstance(client, AsyncOpenAI)` 且 `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` 上无 `api_version` | 彻底移除 |
| `isinstance(client, AsyncAzureOpenAI)` | 客户端类型已变更 | `isinstance(client, AsyncOpenAI)` |

---

## 4. 更新测试夹具中的环境变量

测试通常通过 `monkeypatch.setenv` 设置环境变量。更新如下：

| 旧环境变量 | 新环境变量 | 备注 |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | 标准 Azure 身份 SDK 约定 |
| `AZURE_OPENAI_VERSION` | 移除 | 不需要 `api_version` |
| `AZURE_OPENAI_API_VERSION` | 移除 | 不需要 `api_version` |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | 保留（仍用于 `base_url`） |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | 保留（`model` 参数的部署名称） |

---

## 5. 搜索需要迁移的测试代码

```bash
# 特定于测试的遗留模式
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
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->