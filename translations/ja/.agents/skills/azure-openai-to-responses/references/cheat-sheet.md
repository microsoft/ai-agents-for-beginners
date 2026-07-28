# Responses API チートシート（Python + Azure OpenAI）

> 以下のすべてのコードスニペットは、`deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]` を前提としており、`client` はすでに初期化済み（クライアントセットアップを参照）です。

## 基本的なリクエスト
```python
resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## クライアントセットアップ — EntraID（推奨）
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import OpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = OpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## クライアントセットアップ — APIキー
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

## 非同期クライアントセットアップ — EntraID
```python
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AsyncOpenAI

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 非同期クライアントセットアップ — 明示的なテナント指定ありのEntraID（マルチテナント）

Azure OpenAIリソースがデフォルトのテナントとは<strong>異なるテナント</strong>にある場合、資格情報に対して `tenant_id` を明示的に渡します。これは、開発者のホームテナントとリソースのテナントが異なる開発やテストシナリオで一般的です。

```python
import os
from azure.identity.aio import (
    AzureDeveloperCliCredential,
    ChainedTokenCredential,
    ManagedIdentityCredential,
    get_bearer_token_provider,
)
from openai import AsyncOpenAI

# 本番環境用の ManagedIdentityCredential（Azure Container Apps、App Service など）
managed_identity_cred = ManagedIdentityCredential(
    client_id=os.getenv("AZURE_CLIENT_ID")  # ユーザー割り当てのマネージドID
)
# ローカル開発用の AzureDeveloperCliCredential — 明示的な tenant_id が重要
azd_cred = AzureDeveloperCliCredential(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    process_timeout=60,
)
# チェーン: まずマネージドIDを試し、azd CLI をフォールバックとして使用する
azure_credential = ChainedTokenCredential(managed_identity_cred, azd_cred)

token_provider = get_bearer_token_provider(
    azure_credential, "https://cognitiveservices.azure.com/.default"
)

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)
```

## 非同期クライアント移行 — 変更前/変更後

変更前（非推奨）:
```python
from openai import AsyncAzureOpenAI

client = AsyncAzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_ad_token_provider=token_provider,
)

resp = await client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

変更後:
```python
from openai import AsyncOpenAI

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = AsyncOpenAI(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=token_provider,
)

resp = await client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## フル同期移行 — 変更前/変更後

変更前（レガシー — Azure OpenAI Chat Completions）:
```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

resp = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

変更後（Responses API — Azure OpenAI v1エンドポイント）:
```python
from openai import OpenAI
import os

deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

resp = client.responses.create(
    model=deployment,
    input="Hello",
    max_output_tokens=1000,
    store=False,
)
print(resp.output_text)
```

## ストリーミング（同期）
```python
stream = client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()  # 行末の改行
```

## ストリーミング（非同期）
```python
stream = await client.responses.create(
    model=deployment,
    input="Explain streaming in simple terms",
    max_output_tokens=1000,
    stream=True,
)
async for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
```

## Webアプリのストリーミング — バックエンドからフロントエンドへの形状

SSE/JSONLをフロントエンドにストリーミングするWebアプリを移行する際、<strong>バックエンドのシリアライズ形式</strong>は変わります。バックエンドの新しい出力を、フロントエンドの既存のアクセスパターンを維持するよう設計して、フロントエンドに変更を加える必要がないようにしてください。

<strong>変更前</strong> — Chat Completionsのバックエンドは通常、各チャンクの `choices[0]` 辞書をシリアライズしていました:
```python
# 古い: チャンクごとのシリアライズされた完全な選択辞書
async for chunk in response:
    if chunk.choices:
        yield json.dumps(chunk.choices[0].model_dump()) + "\n"
```
フロントエンドの読み取り: `response.delta.content`（choiceオブジェクトの深いパス）。

<strong>変更後</strong> — Responses APIのバックエンドは、同じフロントエンドアクセスパスを維持する最小限の形状を出力します:
```python
# 新規: フロントエンドが必要とするものだけを出力する
async for event in await chat_coroutine:
    if event.type == "response.output_text.delta":
        yield json.dumps({"delta": {"content": event.delta}}) + "\n"
    elif event.type == "response.completed":
        yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
```
フロントエンドは引き続き `response.delta.content` を読むため、<strong>フロントエンドに変更は不要</strong>です。

> <strong>重要な洞察</strong>: Responses APIのストリーミング形状（`event.type` + `event.delta`）は、Chat Completions（`chunk.choices[0].delta.content`）とは根本的に異なります。ただし、バックエンドからフロントエンドへの契約は開発者が定義するものです。バックエンド出力をフロントエンドが期待する形に合わせて形成してください。

## ストリーミングイベントのシーケンス

`stream: true` の場合、APIは次の順序でイベントを発行します:
1. `response.created` – レスポンスオブジェクト初期化済み
2. `response.in_progress` – 生成開始
3. `response.output_item.added` – 出力アイテムが作成された
4. `response.content_part.added` – コンテンツパート開始
5. `response.output_text.delta` – テキストチャンク（複数あり、各チャンクは `delta: string` を含む）
6. `response.output_text.done` – テキスト生成が完了
7. `response.content_part.done` – コンテンツパート終了
8. `response.output_item.done` – 出力アイテム終了
9. `response.completed` – 全レスポンス完了

基本的なテキストストリーミングでは、テキストチャンクのために `response.output_text.delta` と、完了のために `response.completed` のみを処理します。

## Webアプリにおけるストリーミングエラー処理

Webアプリでストリーミングを行う場合、非同期イテレーションを `try/except` でラップし、エラーをJSONとして発行してフロントエンドが適切に表示できるようにします（例：レート制限、一時的な失敗など）：

```python
@stream_with_context
async def response_stream():
    chat_coroutine = client.responses.create(
        model=deployment,
        input=all_messages,
        max_output_tokens=1000,
        stream=True,
        store=False,
    )
    try:
        async for event in await chat_coroutine:
            if event.type == "response.output_text.delta":
                yield json.dumps({"delta": {"content": event.delta}}) + "\n"
            elif event.type == "response.completed":
                yield json.dumps({"delta": {"content": None}, "finish_reason": "stop"}) + "\n"
    except Exception as e:
        current_app.logger.error(e)
        yield json.dumps({"error": str(e)}) + "\n"
```

> <strong>重要な理由</strong>: Azure OpenAIはレート制限時に `429 Too Many Requests` を返します。`try/except` がないとストリーミングレスポンスは無言で中断しますが、これを入れるとフロントエンドは `{"error": "Too Many Requests"}` を受け取り、再試行プロンプトを表示できます。

## ストリーミングイベントタイプ（Python SDK）

- `ResponseTextDeltaEvent`: `type='response.output_text.delta'`, `delta: str`
- `ResponseCompletedEvent`: `type='response.completed'`, `response: Response`

## 会話フォーマット
```python
# Responses API は入力配列を通じて会話形式をサポートします
response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are an Azure cloud architect."},
        {"role": "user", "content": "Design a scalable web application architecture."},
    ],
    max_output_tokens=1000,
)
print(response.output_text)
```

## コンテンツフィルターエラーの処理

エラーボディの構造はChat CompletionsからResponses APIに変わりました。

変更前（Chat Completions）:
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["innererror"]["content_filter_result"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

変更後（Responses API）:
```python
except openai.APIError as error:
    if error.code == "content_filter":
        if error.body["content_filters"][0]["content_filter_results"]["jailbreak"]["filtered"] is True:
            print("Jailbreak detected!")
```

主な違い:
- `innererror` のラッパーは<strong>なくなり</strong> — コンテンツフィルターの詳細は `error.body` のトップレベルにあります。
- `content_filter_result`（単数）→ `content_filters`（複数の配列）に変わり、それぞれのエントリ内に `content_filter_results`（複数）を含みます。
- 各 `content_filters` のエントリには `blocked`、`source_type`、およびカテゴリごとの詳細（`jailbreak`、`hate`、`sexual`、`violence`、`self_harm`）を含む `content_filter_results` が含まれます。

完全なResponses APIのコンテンツフィルターエラーのボディ形状:
```json
{
  "message": "The response was filtered...",
  "type": "invalid_request_error",
  "param": "prompt",
  "code": "content_filter",
  "content_filters": [
    {
      "blocked": true,
      "source_type": "prompt",
      "content_filter_results": {
        "jailbreak": { "detected": true, "filtered": true },
        "hate": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ]
}
```

## 生のHTTP移行（requests/httpx）

SDKを使わずにアプリが直接Azure OpenAI RESTに呼び出しを行う場合:

変更前（Chat Completions）:
```python
endpoint = f"{azure_endpoint}/openai/deployments/{deployment}/chat/completions?api-version=2024-03-01-preview"
data = {
    "messages": [{"role": "user", "content": query}],
    "model": model_name,
    "temperature": 0,
}
response = requests.post(endpoint, headers=headers, json=data)
message = response.json()["choices"][0]["message"]["content"]
```

変更後（Responses API）:
```python
endpoint = f"{azure_endpoint}/openai/v1/responses"
data = {
    "model": deployment,
    "input": [{"role": "user", "content": query}],
    "temperature": 0,
    "max_output_tokens": 1000,
    "store": False,
}
response = requests.post(endpoint, headers=headers, json=data)
output_text = response.json()["output"][0]["content"][0]["text"]
```

> <strong>注意</strong>: `output_text` はPython SDKの `Response` オブジェクト上の便利なプロパティです。生のREST JSONレスポンスにはトップレベルの `output_text` フィールドはなく、テキストは `output[0].content[0].text` にあります。

## マルチターン会話
```python
# Responses APIで会話を構築する
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Write a Python function to calculate factorial"},
]

response = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)

# アシスタントの応答を会話に追加する
messages.append({"role": "assistant", "content": response.output_text})

# 会話を続ける
messages.append({"role": "user", "content": "Now optimize it with memoization"})

response2 = client.responses.create(
    model=deployment,
    input=messages,
    max_output_tokens=400,
)
print(response2.output_text)
```

コンテンツタイプ付きマルチターン（明示的な `input_text`/`output_text`）:
```python
messages = [
    {"role": "system", "content": [{"type": "input_text", "text": "You are helpful."}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Hi"}]},
    {"role": "assistant", "content": [{"type": "output_text", "text": "Hello!"}]},
    {"role": "user", "content": [{"type": "input_text", "text": "Tell me a joke"}]},
]
resp = client.responses.create(model=deployment, input=messages, store=False)
```

### `previous_response_id` を使ったマルチターン（代替）

会話配列を自分で管理する代わりに、サーバー側で `previous_response_id` を使ってレスポンスをチェーンできます。APIは各レスポンスを保存し、以前のターンを自動的に先頭に付加します。



```python
# 最初のターン
response = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Write a Python function to calculate factorial"}],
)
print(response.output_text)

# 以降のターン — 新しいユーザーメッセージと前回の応答IDを渡すだけ
response2 = client.responses.create(
    model=deployment,
    input=[{"role": "user", "content": "Now optimize it with memoization"}],
    previous_response_id=response.id,
)
print(response2.output_text)
```

**どちらを使うべきか：**

| 方法 | 利点 | 欠点 |
|---|---|---|
| `input` 配列（手動） | 履歴の完全な制御が可能；トリムや要約が可能；サーバー側の保存不要 (`store=False`) | コードが増える；配列を管理する必要がある |
| `previous_response_id` | コードがシンプル；自動チェーン可能 | `store=True`（デフォルト）が必要；会話はサーバー側に保存される；ターン間の履歴変更は不可 |

> **移行メモ:** ほとんどのChat Completionsアプリはすでに自分でメッセージ配列を管理しているため、`input` 配列への変換はより直接的な1対1の移行です。会話履歴の操作が不要な新しいコードや場合には `previous_response_id` を使います。

## Oシリーズ推論モデル（o1, o3-mini, o3, o4-mini）

OシリーズモデルはResponses APIに移行する際に独自のパラメータ制約があります。

### Oシリーズのパラメータマッピング

| Chat Completions（oシリーズ） | Responses API | 備考 |
|---|---|---|
| `max_completion_tokens` | `max_output_tokens` | 大きめに設定（4096以上）— 推論トークンは制限に含まれます |
| `reasoning_effort` | `reasoning.effort` | 存在すればそのまま使用（low/medium/high） |
| `temperature` | 削除または `1` に設定 | Oシリーズは `1` のみ許容 |
| `top_p` | 削除 | Oシリーズは未対応 |
| `seed` | 削除 | Responses APIでは未対応 |

### Oシリーズの変更前/変更後

変更前（Chat Completionsでのoシリーズ）:
```python
resp = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Solve this step by step: 2x + 5 = 13"}],
    max_completion_tokens=4096,
    reasoning_effort="medium",
)
print(resp.choices[0].message.content)
```

変更後（Responses API）:
```python
resp = client.responses.create(
    model=deployment,
    input="Solve this step by step: 2x + 5 = 13",
    max_output_tokens=4096,
    reasoning={"effort": "medium"},
    store=False,
)
print(resp.output_text)
```

> <strong>注意</strong>: Oシリーズモデルは推論中に出力をバッファリングし、テキストデルタを発行する前に一定の遅延が生じることがあります。ストリーミング自体は動作しますが、最初の `response.output_text.delta` イベントはGPTモデルより遅れて届くことがあります。

## 推論トークンへのアクセス
```python
# 推論モデルは内部推論を使用します — 使用された推論トークンの数を見ることができます
response = client.responses.create(
    model=deployment,
    input="Explain quantum computing in simple terms",
    max_output_tokens=1000,
)
print(response.output_text)
print(f"Status: {response.status}")
print(f"Reasoning tokens: {response.usage.output_tokens_details.reasoning_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
```

> <strong>重要</strong>: 内部推論処理を考慮して、`max_output_tokens=1000`（50～200ではなく）を使用してください。モデルは最終出力を生成する前に内部的に推論トークンを使用します。

## 構造化出力 — JSONスキーマ
```python
resp = client.responses.create(
    model=deployment,
    input="What is the capital of France?",
    max_output_tokens=500,
    text={
        "format": {
            "type": "json_schema",
            "name": "Output",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"answer": {"type": "string"}},
                "required": ["answer"],
                "additionalProperties": False,
            },
        }
    },
    store=False,
)
import json
data = json.loads(resp.output_text)
print(data["answer"])
```

## ツールの使用

- `tools` に定義する関数は **フラットなResponses APIフォーマット** に従う — `name`、`description`、`parameters` はトップレベル（`function` にネストしない）。
- モデルがツール呼び出しを要求したら、アプリで実行し、ツールの結果を次のリクエストの `input` 内の `function_call_output` アイテムとして含める。
- スキーマは最小限にし、実行前に入力の検証を行う。
- `strict: true` を使う場合、すべてのプロパティは `required` にリストアップし、`additionalProperties: false` を必須とする。

> **⚠️ `pydantic_function_tool()` は非対応**: `openai.pydantic_function_tool()` ヘルパーは旧Chat Completionsのネスト形式（`{"type": "function", "function": {"name": ...}}`）を生成し続けています。`responses.create()` と一緒に使わないでください。ツールスキーマは手動定義するかラッパーでフラットに変換してください。

### ツール定義フォーマット

Responses APIは<strong>フラット</strong>なツールフォーマットを採用 — `name`、`description`、`parameters` はトップレベルキー（`function` にネストしない）。

**変更前（Chat Completions — ネスト型）:**
```python
tools = [{"type": "function", "function": {"name": "lookup_weather", "parameters": {...}}}]
```

**変更後（Responses API — フラット）:**
```python
tools = [{"type": "function", "name": "lookup_weather", "parameters": {...}}]
```

完全な例:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model=deployment,
    input=[
        {"role": "system", "content": "You are a weather chatbot."},
        {"role": "user", "content": "What's the weather in Berkeley?"},
    ],
    tools=tools,
    tool_choice="auto",
    store=False,
)
```

`strict: true`（スキーマ厳密適用）付き:
```python
tools = [
    {
        "type": "function",
        "name": "lookup_weather",
        "description": "Lookup the weather for a given city name.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {"type": "string", "description": "The city name"},
            },
            "required": ["city_name"],       # すべてのプロパティを列挙する必要があります
            "additionalProperties": False,   # 厳密モードで必須です
        },
    }
]
```

### ツール呼び出しの往復（実行して結果を返す）

モデルがツール呼び出しを要求した場合、`response.output` アイテム＋`function_call_output` を使用してください — Chat Completionsの `role: assistant` + `role: tool` パターン<strong>ではありません</strong>。

```python
import json

messages = [
    {"role": "system", "content": "You are a weather chatbot."},
    {"role": "user", "content": "Is it sunny in Berkeley?"},
]

response = client.responses.create(
    model=deployment, input=messages, tools=tools, store=False,
)

tool_calls = [item for item in response.output if item.type == "function_call"]
if tool_calls:
    # モデルの function_call 項目を会話に追加する
    messages.extend(response.output)

    # 各ツールを実行して結果を追加する
    for tc in tool_calls:
        result = execute_tool(tc.name, json.loads(tc.arguments))
        messages.append({
            "type": "function_call_output",
            "call_id": tc.call_id,
            "output": json.dumps(result),
        })

    # ツールの結果を使って最終応答を取得する
    response = client.responses.create(
        model=deployment, input=messages, tools=tools, store=False,
    )
    print(response.output_text)
```

### Few-shot ツール呼び出し例

`input` にツール呼び出しのfew-shot例を提供する際は、`function_call` と `function_call_output` アイテムを使います。IDは `fc_` で始まる必要があります。

```python
messages = [
    {"role": "system", "content": "You are a product search assistant."},
    {"role": "user", "content": "Find climbing gear for outdoors"},
    {
        "type": "function_call",
        "id": "fc_example1",
        "call_id": "call_example1",
        "name": "search_database",
        "arguments": '{"search_query": "climbing gear outdoor"}',
    },
    {
        "type": "function_call_output",
        "call_id": "call_example1",
        "output": "Results: ...",
    },
    {"role": "user", "content": "Now find shoes under $50"},
]
```

```python
# 組み込みのウェブ検索の例
resp = client.responses.create(
    model=deployment,
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
    store=False,
)
print(resp.output_text)
```

## 画像入力

画像コンテンツアイテムはタイプが `image_url` から `input_image` に変わり、URLはネストされたオブジェクトからフラットな文字列に変わります。

### 画像入力 — 変更前（Chat Completions）
```python
resp = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=500,
)
print(resp.choices[0].message.content)
```

### 画像入力 — 変更後（Responses API、URL）
```python
resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://example.com/image.jpg",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

### 画像入力 — 変更後（Responses API、base64）
```python
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image("path_to_your_image.jpg")

resp = client.responses.create(
    model=deployment,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    max_output_tokens=500,
    store=False,
)
print(resp.output_text)
```

> <strong>主な変更点</strong>: (1) `"type": "image_url"` → `"type": "input_image"`, (2) `"image_url": {"url": "..."}`（ネストオブジェクト）→ `"image_url": "..."`（フラット文字列 — HTTPS URL か `data:image/...;base64,...` のデータURI）、(3) `"type": "text"` → `"type": "input_text"`。

## Microsoft Agent Framework (MAF) 移行

**まずMAFのバージョンを確認してください** — 移行内容はMAF 1.0.0+かそれ以前のベータ/RCかによって異なります。

確認方法: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

MAF 1.0.0+では、`OpenAIChatClient` は<strong>すでにResponses APIを使用している</strong>ため移行は不要です。

レガシーな `OpenAIChatCompletionClient`（`chat.completions.create` を使用）を使っている場合は、`OpenAIChatClient` に置き換えてください:

変更前:
```python
from agent_framework.openai import OpenAIChatCompletionClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatCompletionClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

変更後:
```python
from agent_framework.openai import OpenAIChatClient
from azure.identity.aio import DefaultAzureCredential, get_bearer_token_provider

async_credential = DefaultAzureCredential()
token_provider = get_bearer_token_provider(async_credential, "https://cognitiveservices.azure.com/.default")

client = OpenAIChatClient(
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT']}/openai/v1/",
    api_key=token_provider,
    model=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
)
```

### MAF pre-1.0.0（ベータ/RCリリース）

pre-1.0.0のMAFでは `OpenAIChatClient` がChat Completionsを使用していました。`agent-framework-openai>=1.0.0` にアップグレードすると、`OpenAIChatClient` はデフォルトでResponses APIを使用します。

> <strong>注意</strong>: `Agent`、`MCPStreamableHTTPTool`、その他のMAF APIには変更はなく、クライアントクラスのインポートとインスタンス生成のみが変更されます。

## LangChain（`langchain-openai`）移行

`ChatOpenAI()` に `use_responses_api=True` を追加します。またメッセージの内容アクセスを `.content` から `.text` に更新します。

変更前:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
)

# ... エージェントの呼び出し ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].content)
```

変更後:
```python
import azure.identity
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

token_provider = azure.identity.get_bearer_token_provider(
    azure.identity.DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
model = ChatOpenAI(
    model=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    base_url=os.environ["AZURE_OPENAI_ENDPOINT"] + "/openai/v1/",
    api_key=token_provider,
    use_responses_api=True,
)

# ... エージェント呼び出し ...
result = await agent.ainvoke({"messages": [HumanMessage(content=query)]})
print(result['messages'][-1].text)
```

> <strong>主な変更点</strong>: (1) コンストラクターに `use_responses_api=True`、(2) レスポンスメッセージの `.content` → `.text`。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->