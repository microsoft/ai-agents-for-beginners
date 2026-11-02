# テストインフラ移行

Chat Completions から Responses API へコードベースを移行する際、<strong>テストは予測可能な形で壊れます</strong>。このリファレンスは修正すべき点をカバーします。

---

## ストリーミングレスポンスのモック (Python pytest)

### コアモッククラス

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
            # 空白を保持する: 最初の単語以外のすべての単語の前にスペースを追加する
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

### メッセージ内容によるモックレスポンスのルーティング

実際のアプリはプロンプトに基づき異なる回答を提供します。`messages` ではなく `input` によってルーティングしてください：

```python
async def mock_acreate(*args, **kwargs):
    # レスポンスAPIは 'messages' ではなく 'input' を使用します
    last_message = kwargs.get("input", [])[-1]["content"]
    if last_message == "What is the capital of France?":
        return AsyncResponseIterator("The capital of France is Paris.")
    elif last_message == "What is the capital of Germany?":
        return AsyncResponseIterator("The capital of Germany is Berlin.")
    else:
        raise ValueError(f"Unexpected message: {last_message}")
```

### Monkeypatch パス

| クライアントタイプ | Monkeypatch パス |
|-------------|------------------|
| `AsyncOpenAI` | `openai.resources.responses.AsyncResponses.create` |
| `OpenAI` (同期) | `openai.resources.responses.Responses.create` |

> <strong>以前</strong> (Chat Completions): `openai.resources.chat.AsyncCompletions.create`
> <strong>以降</strong> (Responses): `openai.resources.responses.AsyncResponses.create`

### フルフィクスチャ例

```python
@pytest.fixture
def mock_openai_responses(monkeypatch):
    # ... ここに MockResponseEvent と AsyncResponseIterator クラス ...

    async def mock_acreate(*args, **kwargs):
        last_message = kwargs.get("input", [])[-1]["content"]
        if last_message == "What is the capital of France?":
            return AsyncResponseIterator("The capital of France is Paris.")
        else:
            raise ValueError(f"Unexpected message: {last_message}")

    monkeypatch.setattr("openai.resources.responses.AsyncResponses.create", mock_acreate)
```

---

## 1. モックフィクスチャを更新する

`ChatCompletionChunk` ベースのモックを上記の `MockResponseEvent` / `AsyncResponseIterator` パターンに置き換えます。主な変更点：

| 以前 (Chat Completions モック) | 以降 (Responses モック) |
|-------------------------------|------------------------|
| `openai.types.chat.ChatCompletionChunk(...)` | `MockResponseEvent(event_type, delta)` |
| `choices[0].delta.content` | `event.delta` |
| チャンク内の `finish_reason="stop"` | `event.type == "response.completed"` |
| Azure特有の `prompt_filter_results` チャンク | 完全に削除 |
| Azure特有の選択ごとの `content_filter_results` | 完全に削除 |
| モック内の `kwargs.get("messages")` | モック内の `kwargs.get("input")` |

---

## 2. スナップショット / ゴールデンファイルを更新する

テストスイートでスナップショットテスト（例：`pytest-snapshot`、syrupy、手作りJSONLスナップショット）を使っている場合、期待される出力の形状が変わります：

<strong>以前</strong> (Chat Completions ストリーミングJSONL):
```jsonl
{"delta": {"content": null, "function_call": null, "refusal": null, "role": "assistant", "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {}}
{"delta": {"content": "The", "function_call": null, "refusal": null, "role": null, "tool_calls": null}, "finish_reason": null, "index": 0, "logprobs": null, "content_filter_results": {"hate": {"filtered": false, "severity": "safe"}, ...}}
{"delta": {"content": null, ...}, "finish_reason": "stop", "index": 0, "logprobs": null, "content_filter_results": {}}
```

<strong>以降</strong> (Responses API ストリーミングJSONL):
```jsonl
{"delta": {"content": "The"}}
{"delta": {"content": " capital"}}
{"delta": {"content": null}, "finish_reason": "stop"}
```

新しい形状は劇的にシンプルです — `function_call`、`refusal`、`role`、`tool_calls`、`index`、`logprobs`、`content_filter_results` のフィールドはありません。すべてのスナップショットファイルを更新または再生成してください。

> <strong>ヒント</strong>: 移行後は `--snapshot-update` (pytest-snapshot) または `--update-snapshots` (syrupy) を付けてテストを実行し、自動再生成しましょう。

---

## 3. テストアサーションを更新する

よくあるアサーションの障害：

| 旧アサーション | 問題点 | 新アサーション |
|--------------|---------|---------------|
| `client._azure_ad_token_provider is not None` | `AsyncOpenAI` に `_azure_ad_token_provider` 属性なし | `isinstance(client, AsyncOpenAI)` および `"/openai/v1/" in str(client.base_url)` |
| `client.api_version == "2024-..."` | `OpenAI`/`AsyncOpenAI` に `api_version` なし | 完全に削除 |
| `isinstance(client, AsyncAzureOpenAI)` | クライアントタイプが変更された | `isinstance(client, AsyncOpenAI)` |

---

## 4. テストフィクスチャ内の環境変数を更新する

テストはしばしば `monkeypatch.setenv` で環境変数をセットします。これらを更新してください：

| 旧環境変数名 | 新環境変数名 | 備考 |
|-------------|-------------|-------|
| `AZURE_OPENAI_CLIENT_ID` | `AZURE_CLIENT_ID` | 標準Azure Identity SDKの規約 |
| `AZURE_OPENAI_VERSION` | 削除 | `api_version` は不要 |
| `AZURE_OPENAI_API_VERSION` | 削除 | `api_version` は不要 |
| `AZURE_OPENAI_ENDPOINT` | `AZURE_OPENAI_ENDPOINT` | 維持（`base_url`に必要） |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | `AZURE_OPENAI_CHAT_DEPLOYMENT` | 維持（`model`パラメーターのデプロイ名用） |

---

## 5. 移行が必要なテストコードを検索する

```bash
# テスト固有のレガシーパターン
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
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->