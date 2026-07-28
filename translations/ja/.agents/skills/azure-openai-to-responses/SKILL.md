---
name: azure-openai-to-responses
license: MIT
---
# Azure OpenAI Chat Completions から Responses API への Python アプリ移行

> **正式な指示 — 正確に従うこと**
>
> このスキルは Azure OpenAI Chat Completions を使用している Python コードベースを
> 統一された Responses API に移行します。指示に正確に従ってください。
> パラメータのマッピングを即興で行ったり、API 形状を独自に作成しないでください。

---

## トリガー

ユーザーが以下を望むときにこのスキルを有効にします:
- Azure OpenAI Chat Completions から Responses API へ Python アプリを移行する
- Python の OpenAI SDK の使用を最新の Azure OpenAI 用 API 形状にアップグレードする
- Azure で Responses が必要な GPT-5 以降のモデルに備えて Python コードを準備する
- `AzureOpenAI`/`AsyncAzureOpenAI` から標準の `OpenAI`/`AsyncOpenAI` クライアントの v1 エンドポイントに切り替える
- `AzureOpenAI` のコンストラクターや `api_version` に関する廃止警告を修正する

---

## ⚠️ モデル互換性 — まず確認すること

> **移行前に、Azure OpenAI 配備が Responses API をサポートしているか確認してください。**

### 1. 配備のスモークテスト（最速）

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> <strong>注意</strong>: Azure OpenAI では `max_output_tokens` の<strong>最小値は16</strong>です。16未満は400エラーになります。スモークテストでは50以上を使用してください。

これが 404 を返す場合、その配備のモデルはまだ Responses に対応していません — 下記参照か対応モデルで再配備してください。

### 2. お住まいのリージョンの利用可能モデルを確認（推奨）

標準のモデル互換性ツールを実行して、お住まいのリージョンで Responses API 対応モデルを確認してください:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

これは Azure ARM のライブデータを問い合わせ、対応表を示します — Responses、構造化出力、ツールなどの対応状況が分かります。`--filter gpt-5.1,gpt-5.2` で絞り込み、`--json` でスクリプト処理可能です。

### 3. 全モデルサポート参照

- <strong>ライブクエリ</strong>: `python migrate.py models` （上記参照 — リージョン別、常に最新）
- <strong>利用可否ブラウズ</strong>: [モデルの概要表とリージョン別可用性](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- <strong>クイックスタートとガイダンス</strong>: **https://aka.ms/openai/start**

### ⚠️ 古いモデルの制限

> <strong>警告</strong>: 古いモデル（`gpt-4.1` より前のもの）は Responses API の全機能を完全にサポートしていない場合があります。
>
> 古いモデルの既知の制限:
> - **`reasoning` パラメーター**: 多くの reasoninng 非対応モデルではサポートされません。元のコードに `reasoning` があればそれを移行してください。
> - **`seed` パラメーター**: Responses API では全くサポートされていません — 全リクエストから削除してください。
> - **`text.format` による構造化出力**: 古いモデルは `strict: true` JSON スキーマを確実に適用しません。
> - <strong>ツールオーケストレーション</strong>: GPT-5+ は内部推論の一部としてツール呼び出しを統合します。古いモデルは Responses で動作しますが深い統合はありません。
> - <strong>温度制約</strong>: `gpt-5` へ移行時は temperature を省略するか `1` に設定してください。古いモデルはこの制約がありません。

### Oシリーズ推論モデル (o1, o3-mini, o3, o4-mini)

Oシリーズモデルには特殊なパラメーター制約があります。Oシリーズモデルを対象とするアプリを移行するとき:

- **`temperature`**: `1` にするか省略してください。Oシリーズは他の値を受け付けません。
- **`max_completion_tokens` → `max_output_tokens`**: Azure固有の `max_completion_tokens` は `max_output_tokens` に切り替えが必要。推論トークンもカウントするため大きな値（4096以上）を指定してください。
- **`reasoning_effort`**: アプリが `reasoning_effort`（low/medium/high）を使っている場合、そのまま維持してください — Responses API は Oシリーズでこのパラメーターをサポートします。
- <strong>ストリーミング動作</strong>: Oシリーズは推論終了まで出力をバッファしてからテキスト差分イベントを送る場合があります。ストリーミングは機能しますが、最初の `response.output_text.delta` が GPT モデルより遅れることがあります。
- **`top_p`**: Oシリーズはサポートしません — 存在すれば削除してください。
- <strong>ツールの利用</strong>: Oシリーズモデルは Responses API 経由で GPT モデルと同様にツールをサポートしますが、モデルごとにツール呼び出しのオーケストレーション品質は異なります。

**対応 — 事前のモデルアドバイス**: スキャン段階でアプリがターゲットとするモデル（配備名、環境変数、設定）を確認してください。`gpt-4.1` より古いモデルの場合（gpt-4.1以上でない場合）、ユーザーに次のことを伝えましょう:
- 移行は現在のモデルで基本的なテキスト・チャット・ストリーミング・ツールで動作します。
- 新しいモデル（`gpt-5.1`、`gpt-5.2`）はより良いツールオーケストレーション、構造化出力の強制、推論、リージョン横断可用性を提供します。
- 準備ができたら配備のアップグレードを検討してください — 移行を妨げるものではありません。

モデルバージョンを理由に移行を拒否・ブロックしないでください。この案内は情報提供のみです。

### GitHub Models は Responses API をサポートしません

> **GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) は Responses API をサポートしていません。**

もしコードベースに GitHub Models のコードパスがある場合（`base_url` が `models.github.ai` または `models.inference.ai.azure.com` を指している）、<strong>移行時に完全に削除してください</strong>。Responses API は Azure OpenAI、OpenAI、または対応するローカルエンドポイント（例：Responses対応の Ollama）が必要です。

スキャン時のアクション:
- GitHub Models のコードパスは削除対象としてマークしてください。

---

## フレームワークの移行

多くのアプリは OpenAI の上に高レベルのフレームワークを使っています。これらを移行するときは、フレームワーク自身の API 変更にも注意が必要で、単に基底の OpenAI 呼び出しを置き換えるだけではありません。

### Microsoft Agent Framework (MAF)

**まず MAF のバージョンを確認してください** — 移行は MAF 1.0.0 以降か、それ以前のベータ/RCかによって異なります。

#### MAF 1.0.0 以降 (agent-framework-openai >= 1.0.0)

`OpenAIChatClient` は **すでに Responses API を使用しています** — 移行不要です。レガシーの `OpenAIChatCompletionClient`（`chat.completions.create` を使う）を使っている場合は `OpenAIChatClient` に置き換えてください。

| 以前 | 以降 |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

バージョン確認コマンド: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF 1.0.0 未満 (ベータ/RC リリース)

1.0.0 未満の MAF では `OpenAIChatClient` が Chat Completions を使っていました。`agent-framework-openai>=1.0.0` にアップグレードすると `OpenAIChatClient` はデフォルトで Responses API を使います。

他の変更は不要です — `Agent` とツールの API は変わりません。

### LangChain (`langchain-openai`)

`ChatOpenAI()` に `use_responses_api=True` を追加し、レスポンスアクセスを `.content` から `.text` に変更してください。

| 以前 | 以降 |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

完全な変更例は [cheat-sheet.md](./references/cheat-sheet.md) を参照してください。

---

## フロントエンド移行ガイダンス

> **Responses API はサーバーサイドの関心事です。** Python バックエンドを移行してください。フロントエンドの HTTP 契約はバックエンドが薄いパススルーでない限り変更不要です — もしそうなら、Responses リクエスト形状の採用を検討し、翻訳レイヤーをなくしてください。フロントエンドがクライアント側のキーで OpenAI を直接呼び出している場合は、まずバックエンドで呼び出すようにしてください。

### `@microsoft/ai-chat-protocol` の廃止

`@microsoft/ai-chat-protocol` npm パッケージは廃止されており、[`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) に置き換えるべきです。フロントエンドで見つけたら:

1. CDNスクリプトタグを置き換える:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. `AIChatProtocolClient` のインスタンス生成 (`new ChatProtocol.AIChatProtocolClient("/chat")`) を削除する。
3. `client.getStreamedCompletion(messages)` をバックエンドのストリーミングエンドポイントへの直接 `fetch()` 呼び出しに置き換える。
4. `for await (const response of result)` を `for await (const chunk of readNDJSONStream(response.body))` に置き換える。
5. プロパティアクセスを `response.delta.content` / `response.error` から `chunk.delta.content` / `chunk.error` に変更する。

---

## 目的

- Azure OpenAI に対する Chat Completions またはレガシー Completions を使っているすべての Python 呼び出し箇所を列挙する。
- Python コードベースに対し移行計画と順序を提案する。
- Responses API に切り替えるための安全かつ最小限の修正を適用する。
- 呼び出し側を Responses 出力スキーマを消費するように更新する。互換ラッパーは使わない。
- テストやリントを実行し、移行による小さな破壊を修正する。
- 小さくレビューしやすい変更セットを用意し、最終的な差分付きサマリーを提供する（コミットはしない）。

---

## ガードレール

- git ワークスペース内のファイルのみ修正する。外部には書き込まない。
- 後方互換のシムを残さず、新しい API 形状にコードを移行する。
- 墓標/トランジション用コメントやバックアップファイルを残さない。
- 以前ストリーミングを使っていればそのまま維持し、それ以外は非ストリーミングを使用する。
- 承認モードならコマンドやネットワーク呼び出しの実行前に承認を求める。
- `git add`/`git commit`/`git push` は実行しない。作業ツリーの編集のみを行う。

---

## ステップ 0: Azure OpenAI クライアントの移行（事前準備）

コードベースで `AzureOpenAI` や `AsyncAzureOpenAI` のコンストラクターを使っていれば、まず標準の `OpenAI` / `AsyncOpenAI` コンストラクターに移行してください。Azure 固有のコンストラクターは `openai>=1.108.1` で廃止されました。

### なぜ v1 API パスを使うのか？

新しい `/openai/v1` エンドポイントは `AzureOpenAI()` ではなく標準の `OpenAI()` クライアントを使い、`api_version` パラメーターを不要にし、OpenAI と Azure OpenAI の両方で同じ動作を保証します。同じクライアントコードで将来も問題ありません — バージョン管理が不要です。

### 主な変更点

| 以前 | 以降 |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | 完全に削除 |

### クリーンアップチェックリスト

- クライアント構築から `api_version` 引数を削除する。
- `.env`、アプリ設定、Bicep/インフラファイルから `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` 環境変数を削除する。
- `.env`、アプリ設定、Bicep/インフラ、テストフィクスチャで `AZURE_OPENAI_CLIENT_ID` を `AZURE_CLIENT_ID` に名前変更する（標準的な Azure Identity SDK の慣例）。
- `requirements.txt` または `pyproject.toml` に `openai>=1.108.1` を確保する。

### 環境変数移行

| 旧環境変数 | アクション | 備考 |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | <strong>削除</strong> | v1 エンドポイントでは `api_version` 不要 |
| `AZURE_OPENAI_API_VERSION` | <strong>削除</strong> | 上と同じ |
| `AZURE_OPENAI_CLIENT_ID` | <strong>名前変更</strong> → `AZURE_CLIENT_ID` | `ManagedIdentityCredential(client_id=...)` 用の標準慣例 |
| `AZURE_OPENAI_ENDPOINT` | <strong>保持</strong> | `base_url` 構築にまだ必要 |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | <strong>保持</strong> | `responses.create` の `model` パラメーターとして使用 |
| `AZURE_OPENAI_API_KEY` | <strong>保持</strong> | キーベース認証の `api_key` として使用 |

クライアント設定コード例（同期、非同期、EntraID、APIキー、多テナント）は [cheat-sheet.md](./references/cheat-sheet.md) を参照してください。

---

## ステップ 1: レガシー呼び出し箇所の検出

移行が必要なすべての呼び出し箇所を見つけるために [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) スクリプトを実行してください:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

または手動で次の検索を実行してください — マッチしたすべてが移行対象です:

```bash
# レガシーAPI呼び出し（書き換えが必要）
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# 廃止予定のAzureクライアントコンストラクター（置き換えが必要）
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# レスポンス形状アクセスパターン（更新が必要）
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# 古いネスト形式のツール定義（フラット化が必要）
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# 古い形式のツール結果（function_call_outputへの変換が必要）
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# 廃止予定のパラメーター（削除または名前変更が必要）
rg "response_format"
rg "max_tokens\b"        # max_output_tokensに名前変更
rg "['\"]seed['\"]"      # remove entirely

# 廃止予定の環境変数（整理が必要）
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_IDであるべき

# GitHubモデルエンドポイント（削除が必要 — Responses APIは未対応）
rg "models\.github\.ai|models\.inference\.ai\.azure"

# フレームワークレベルのレガシーパターン（更新が必要）
rg "OpenAIChatCompletionClient"  # MAF 1.0.0以降: OpenAIChatClientに置き換え
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=Trueが必要

# テスト基盤（更新が必要）
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# コンテンツフィルターエラーの本文アクセス（更新が必要 — 構造が変更）
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # 古い単数形 — 現在はcontent_filters配列内のcontent_filter_results（複数形）

# Chat Completionsエンドポイントへの生のHTTP呼び出し（URLの更新が必要）
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### ヒューリスティクス（検出と書き換え）

- **Chat Completions クライアント**: `client.chat.completions.create` → `client.responses.create(...)`。

- **Azure クライアントコンストラクター**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`。
- <strong>ツール</strong>: 関数呼び出しツールの定義をネスト形式（`{"type": "function", "function": {"name": ...}}`）からフラットな Responses 形式（`{"type": "function", "name": ...}`）に変換する；`tool_choice` を使用する；ツール結果は `{"type": "function_call_output", "call_id": ..., "output": ...}` アイテムとして返す（`{"role": "tool", ...}` ではない）。
- <strong>ツールの往復処理</strong>: モデルが関数呼び出しを返す場合、会話に `response.output` アイテムを追加する（手動で `{"role": "assistant", "tool_calls": [...]}` 辞書を追加しない）、次に各結果に対して `function_call_output` アイテムを追加する。
- <strong>数ショットのツール例</strong>: 会話にハードコードされたツール呼び出し例が含まれる場合、これらを `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` ＋ `{"type": "function_call_output", ...}` アイテムに変換する。IDは必ず `fc_` で始まる必要がある。
- **`pydantic_function_tool()`**: このヘルパーはまだ旧来のネスト形式を生成し、`responses.create()` と互換性が <strong>ありません</strong>。手動ツール定義かフラット化ラッパーに置き換えること。
- <strong>マルチターン</strong>: 会話履歴はアプリ内で管理し、過去のターンは `input` アイテムとして渡す。
- <strong>フォーマット</strong>: Chat のトップレベル `response_format` を Responses の `text.format` に置き換える。正式な形状は `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`。
- <strong>コンテンツアイテム</strong>: Chat の `content[].type: "text"` は Responses の `content[].type: "input_text"` に置き換える（ユーザー/システムのターン）。
- <strong>画像コンテンツアイテム</strong>: Chat の `content[].type: "image_url"` は Responses の `content[].type: "input_image"` に置き換える。`image_url` フィールドはネストオブジェクト `{"url": "..."}` からフラットな文字列に変更される。前後の例はチートシート参照。
- <strong>推論努力</strong>: **元のコードですでに `reasoning` が存在する場合のみ移行する**。
- <strong>コンテンツフィルターエラー処理</strong>: エラーボディ構造が変更された。Chat Completions は `error.body["innererror"]["content_filter_result"]`（単数）を使用していたが、Responses API では `error.body["content_filters"][0]["content_filter_results"]`（複数、配列内）となる。`innererror` にアクセスするコードは `KeyError` を引き起こす。新しいパスを使うよう書き換えが必要。
- **生の HTTP コール**: アプリが Azure OpenAI REST API を直接（`requests`, `httpx` などで） `/openai/deployments/{name}/chat/completions?api-version=...` 経由で呼び出している場合は `/openai/v1/responses` に書き換える。リクエストボディは `messages` → `input`、`max_output_tokens` と `store: false` を追加、クエリパラメータの `api-version` を削除。レスポンスボディは `choices[0].message.content` → `output[0].content[0].text` に変更（注意：`output_text` は SDK の便宜的プロパティで生の REST JSON には存在しない）。

---

## ステップ 2: 移行の適用

### 移行ノート（Chat Completions → Responses）

- <strong>なぜ移行するのか</strong>: Responses はテキスト、ツール、ストリーミングの統合 API であり、Chat Completions はレガシー。GPT-5 以降は最高性能のために Responses が必須。
- **HTTP**: Azure エンドポイントが `/openai/deployments/{name}/chat/completions` から `/openai/v1/responses` に切り替わる。
- <strong>フィールド</strong>: `messages` → `input`、`max_tokens` → `max_output_tokens`。`temperature` は変更なし。
- <strong>フォーマット</strong>: `response_format` → 適切なオブジェクトの `text.format`。
- <strong>コンテンツアイテム</strong>: Chat の `content[].type: "text"` は Responses の `content[].type: "input_text"` に置換（システム／ユーザーターン）。
- <strong>画像コンテンツアイテム</strong>: Chat の `content[].type: "image_url"` は Responses の `content[].type: "input_image"` に置換。`image_url` フィールドは `{"image_url": {"url": "..."}}` から `{"image_url": "..."}`（プレーンな文字列 — HTTPS URL または `data:image/...;base64,...` のデータ URI）にフラット化。

### パラメーター対応表

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input`（配列） |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format`（オブジェクト） |
| `temperature` | `temperature`（変更なし） |
| `stop` | `stop`（変更なし） |
| `frequency_penalty` | `frequency_penalty`（変更なし） |
| `presence_penalty` | `presence_penalty`（変更なし） |
| `tools` / 関数呼び出し | `tools`（変更なし） |
| `seed` | <strong>削除</strong>（サポートなし） |
| `store` | `store`（`false` に設定） |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."`（フラットな文字列） |

完全な前後のコード例は [cheat-sheet.md](./references/cheat-sheet.md) を参照。

テスト基盤の移行（モック、スナップショット、アサーション）は [test-migration.md](./references/test-migration.md) を参照。

エラー対処や落とし穴は [troubleshooting.md](./references/troubleshooting.md) を参照。

---

## データ保持と状態管理

- 全ての Responses リクエストに `store: false` を設定する。
- 以前のメッセージIDやサーバー保存のコンテキストに依存しない。状態はクライアント管理とし、メタデータを最小化する。

---

## 受け入れ基準

### コードレベルのゲート（全て合格必須）

- [ ] 移行済みファイルで `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` がゼロ。
- [ ] `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` がゼロ — すべてのコンストラクターは v1エンドポイントの `OpenAI`/`AsyncOpenAI` を使用。
- [ ] `rg "models\.github\.ai|models\.inference\.ai\.azure"` がゼロ — GitHub Models のコードパスを削除。
- [ ] `rg "OpenAIChatCompletionClient"` がゼロ — MAF 1.0.0+ のコードは `OpenAIChatClient`（Responses API 使用）。1.0.0未満は `agent-framework-openai>=1.0.0` にアップグレード。
- [ ] 全ての `ChatOpenAI(...)` 呼び出しに `use_responses_api=True` が含まれる。
- [ ] `rg "choices\[0\]"` がゼロ — 全レスポンスアクセスは `resp.output_text` または Responses 出力スキーマ使用。
- [ ] トップレベルに `response_format` がない；構造化出力はすべて `text={"format": {...}}` を使用。
- [ ] `requirements.txt` または `pyproject.toml` に `openai>=1.108.1` と `azure-identity` がある；依存関係を再インストール済み。
- [ ] すべての `responses.create` 呼び出しに `store=False` が設定されている。
- [ ] クライアント構築に `api_version` がない；`AZURE_OPENAI_API_VERSION` は環境ファイルやインフラから削除済み。

### テスト基盤のゲート（全て合格必須）

- [ ] `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` がゼロ。
- [ ] `rg "_azure_ad_token_provider" tests/` がゼロ — アサーションは `isinstance(client, AsyncOpenAI)` または `base_url` を確認に更新済み。
- [ ] `rg "prompt_filter_results|content_filter_results" tests/` がゼロ — Azure特有のフィルターモック削除。
- [ ] モックフィクスチャは `kwargs.get("input")` を使用し、`kwargs.get("messages")` ではない。
- [ ] スナップショット／ゴールデンファイルは Responses ストリーミング形状に更新済み（`choices[0]`, `function_call`, `logprobs` などなし）。
- [ ] `pytest` は全テスト更新後に失敗ゼロで通過。

### 動作ゲート（手動またはテストハーネスで検証）

- [ ] <strong>基本的な完了</strong>: 非ストリーミングの `responses.create` が空でない `output_text` を返す。
- [ ] <strong>ストリームの同等性</strong>: 元コードがストリーミングを使っていた場合、移行コードもストリーミングし、非空のデルタを含む `response.output_text.delta` イベントを生成する。
- [ ] <strong>構造化出力</strong>: `text.format` で `json_schema` を使う場合、`json.loads(resp.output_text)` が成功し、スキーマに合致する。
- [ ] <strong>ツール呼び出しループ</strong>: ツール使用時は、モデルがツール呼び出しを発行し、アプリが実行し、後続リクエストが最終的な `output_text` を返す（無限ループなし）。
- [ ] <strong>非同期の同等性</strong>: `AsyncAzureOpenAI` 使用時は `AsyncOpenAI` の等価物が `await` で動作する。
- [ ] <strong>エラー率</strong>: 移行前ベースラインと比較して新しい 400/401/404 エラーなし。

### 納品物

- 編集したファイル一覧、レガシー呼び出し箇所の移行前後の件数、次のステップを含むサマリー。
- 変更は作業ツリー編集のみ（コミットなし）。

---

## SDK バージョン要件

| パッケージ | 最低バージョン |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | 最新版（EntraID 認証用） |

---

## 参考資料

- [チートシート — 全コードスニペット](./references/cheat-sheet.md)
- [テスト移行 — モック、スナップショット、アサーション](./references/test-migration.md)
- [トラブルシューティング — エラー、リスク表、注意点](./references/troubleshooting.md)
- [detect_legacy.py — 自動スキャナー](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI スターターキット](https://aka.ms/openai/start)
- [Azure OpenAI Responses API ドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API バージョンライフサイクル](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API リファレンス](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->