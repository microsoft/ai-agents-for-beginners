# Microsoft Agent Framework を探る

![Agent Framework](../../../translated_images/ja/lesson-14-thumbnail.90df0065b9d234ee.webp)

### はじめに

このレッスンで扱う内容：

- Microsoft Agent Framework の理解：主要な特徴と価値  
- Microsoft Agent Framework の主要な概念を探る
- 高度な MAF パターン：ワークフロー、ミドルウェア、メモリ

## 学習目標

このレッスンを終えると、次のことができるようになります：

- Microsoft Agent Framework を使って本番対応の AI エージェントを構築する
- Microsoft Agent Framework のコア機能をエージェント用途に適用する
- ワークフロー、ミドルウェア、オブザーバビリティなどの高度なパターンを使用する

## コードサンプル 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) のコードサンプルは、このリポジトリ内の `xx-python-agent-framework` および `xx-dotnet-agent-framework` ファイルにあります。

## Microsoft Agent Framework の理解

![Framework Intro](../../../translated_images/ja/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) は、Microsoft の統一された AI エージェント構築フレームワークです。これは、製品および研究環境で見られる多様なエージェントユースケースに対応する柔軟性を提供します。例えば：

- <strong>逐次的エージェントオーケストレーション</strong>：順を追うワークフローが必要なシナリオにて。
- <strong>同時エージェントオーケストレーション</strong>：エージェントが同時にタスクを完了する必要があるシナリオにて。
- <strong>グループチャットオーケストレーション</strong>：エージェントが一つのタスクを協力して行うシナリオにて。
- <strong>ハンドオフオーケストレーション</strong>：各サブタスクの完了に伴いエージェントがタスクを引き継ぐシナリオにて。
- <strong>マグネティックオーケストレーション</strong>：マネージャーエージェントがタスクリストを作成・修正し、サブエージェントの調整を扱うシナリオにて。

本番環境で AI エージェントを提供するために、MAF には以下の機能も含まれています：

- <strong>オブザーバビリティ</strong>：OpenTelemetry を利用し、AI エージェントのすべてのアクション（ツール呼び出し、オーケストレーションステップ、推論の流れなど）を Microsoft Foundry ダッシュボードで監視可能にします。
- <strong>セキュリティ</strong>：Microsoft Foundry ネイティブホスティングにより、ロールベースアクセス、プライベートデータ処理、組み込みのコンテンツ安全性などのセキュリティ制御を提供します。
- <strong>耐久性</strong>：エージェントスレッドやワークフローは一時停止、再開、エラーからの復旧が可能で、長時間のプロセスをサポートします。
- <strong>制御</strong>：ヒューマンインザループのワークフローをサポートし、人間の承認が必要なタスクをマークできます。

Microsoft Agent Framework はまた、相互運用性に注力しています：

- <strong>クラウド非依存</strong> - エージェントはコンテナ内、オンプレミス、複数の異なるクラウド環境で実行可能です。
- <strong>プロバイダー非依存</strong> - Azure OpenAI や OpenAI を含む好みの SDK を通じてエージェントを作成可能です。
- <strong>オープン標準対応</strong> - Agent-to-Agent (A2A) や Model Context Protocol (MCP) のようなプロトコルを利用して他のエージェントやツールを発見・利用できます。
- <strong>プラグインとコネクター</strong> - Microsoft Fabric、SharePoint、Pinecone、Qdrant といったデータおよびメモリサービスへの接続が可能です。

これらの機能が Microsoft Agent Framework のコア概念のいくつかにどのように適用されているか見てみましょう。

## Microsoft Agent Framework の主要な概念

### エージェント

![Agent Framework](../../../translated_images/ja/agent-components.410a06daf87b4fef.webp)

<strong>エージェントの作成</strong>

エージェントの作成は、推論サービス（LLM プロバイダー）、AI エージェントが従う指示セット、および割り当てられた `name` を定義して行います：


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上記は `Azure OpenAI` を使用していますが、エージェントは `Microsoft Foundry Agent Service` を含む様々なサービスを用いて作成可能です：

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI の `Responses`、`ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

また、[MiniMax](https://platform.minimaxi.com/) のように大きなコンテキストウィンドウ（最大204Kトークン）を備えた OpenAI 互換 API もあります：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

また、A2A プロトコルを使ったリモートエージェントもあります：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>エージェントの実行</strong>

エージェントは、非ストリーミング応答用に `.run`、ストリーミング応答用に `.run_stream` メソッドを使って実行されます。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

各エージェント実行には、エージェントが使用する `max_tokens`、呼び出せる `tools`、および使用する `model` などのカスタムパラメーターをオプションで指定できます。

これは、ユーザーのタスクを完遂するために特定のモデルやツールが必要な場合に便利です。

<strong>ツール</strong>

ツールは、エージェントの定義時に：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgentを直接作成する場合

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

また、エージェント実行時にも定義できます：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # この実行のためだけに提供されたツール)
```

<strong>エージェントスレッド</strong>

エージェントスレッドはマルチターン対話を扱うために使われます。スレッドは以下のいずれかで作成可能です：

- `get_new_thread()` を使用し、スレッドを時間をかけて保存可能にする
- エージェント実行時に自動でスレッドを作成し、その実行時のみスレッドを持たせる

スレッドを作成するコードは次の通りです：

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() # スレッドでエージェントを実行します。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

その後、スレッドを保存用にシリアライズできます：

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() 

# スレッドでエージェントを実行します。

response = await agent.run("Hello, how are you?", thread=thread) 

# ストレージ用にスレッドをシリアライズします。

serialized_thread = await thread.serialize() 

# ストレージから読み込んだ後、スレッドの状態をデシリアライズします。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

<strong>エージェントミドルウェア</strong>

エージェントは、ユーザーのタスクを完了するためにツールや LLM と連携します。特定のシナリオでは、これらのインタラクションの間に処理や追跡を実行したい場合があります。エージェントミドルウェアはこれを可能にします：

<em>関数ミドルウェア</em>

このミドルウェアは、エージェントと呼び出す関数/ツールの間でアクションを実行できるようにします。例としては、関数呼び出し時のログ記録があります。

以下のコードで `next` は次のミドルウェアか実際の関数を呼ぶかを定義します。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 前処理：関数実行前のログ
    print(f"[Function] Calling {context.function.name}")

    # 次のミドルウェアまたは関数の実行へ続行
    await next(context)

    # 後処理：関数実行後のログ
    print(f"[Function] {context.function.name} completed")
```

<em>チャットミドルウェア</em>

このミドルウェアは、エージェントと LLM の間のリクエストでアクションを実行またはログ記録します。

ここには AI サービスに送られる `messages` のような重要な情報が含まれます。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 前処理: AI呼び出し前のログ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 次のミドルウェアまたはAIサービスへ継続
    await next(context)

    # 後処理: AI応答後のログ
    print("[Chat] AI response received")

```

<strong>エージェントメモリ</strong>

`Agentic Memory` レッスンで扱ったように、メモリはエージェントが異なるコンテキストで動作するための重要な要素です。MAF はいくつかの異なるメモリタイプを提供します：

<em>インメモリストレージ</em>

これは、アプリケーション実行時のスレッド内に保存されるメモリです。

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() # スレッドでエージェントを実行します。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>永続メッセージ</em>

これは異なるセッション間の会話履歴保存に使われます。`chat_message_store_factory` を使用して定義します：

```python
from agent_framework import ChatMessageStore

# カスタムメッセージストアを作成する
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

<em>動的メモリ</em>


このメモリはエージェントが実行される前にコンテキストに追加されます。これらのメモリは mem0 のような外部サービスに保存できます。

```python
from agent_framework.mem0 import Mem0Provider

# 高度なメモリ機能のためにMem0を使用する
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

<strong>エージェントの可観測性</strong>

可観測性は信頼性が高く維持可能なエージェントシステムを構築する上で重要です。MAF は OpenTelemetry と統合し、より良い可観測性のためにトレースやメーターを提供します。

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # 何かをする
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ワークフロー

MAF はタスク完了のための事前定義済みステップであるワークフローを提供し、これらのステップのコンポーネントとして AI エージェントを含みます。

ワークフローはより良い制御フローを可能にする異なるコンポーネントで構成されています。ワークフローは <strong>マルチエージェントのオーケストレーション</strong> と <strong>チェックポイント</strong> を可能にしてワークフローの状態を保存します。

ワークフローのコアコンポーネントは以下の通りです：

<strong>エグゼキュータ</strong>

エグゼキュータは入力メッセージを受け取り、割り当てられたタスクを実行し、その後出力メッセージを生成します。これによりワークフローが前進し、より大きなタスクの完了に向かいます。エグゼキュータは AI エージェントまたはカスタムロジックのいずれかです。

<strong>エッジ</strong>

エッジはワークフロー内のメッセージの流れを定義するために使われます。これらは以下のようなものがあります：

<em>ダイレクトエッジ</em> - エグゼキュータ間の単純な1対1の接続：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>条件付きエッジ</em> - ある条件が満たされた後に起動される。例えば、ホテルの部屋が利用できない場合、エグゼキュータは他の選択肢を提案できます。

<em>スイッチケースエッジ</em> - 定義済みの条件に基づいてメッセージを異なるエグゼキュータにルーティングします。例えば、旅行者が優先アクセスを持っている場合、そのタスクは別のワークフローを通じて処理されます。

<em>ファンアウトエッジ</em> - 1つのメッセージを複数のターゲットに送信します。

<em>ファンインエッジ</em> - 複数のエグゼキュータからのメッセージを収集し、1つのターゲットに送信します。

<strong>イベント</strong>

ワークフローの可観測性を高めるために、MAF は以下のような実行イベントを組み込みで提供します：

- `WorkflowStartedEvent`  - ワークフローの実行開始
- `WorkflowOutputEvent` - ワークフローが出力を生成
- `WorkflowErrorEvent` - ワークフローがエラーに遭遇
- `ExecutorInvokeEvent`  - エグゼキュータが処理を開始
- `ExecutorCompleteEvent`  - エグゼキュータが処理を完了
- `RequestInfoEvent` - リクエストが発行される

## 高度な MAF パターン

上記のセクションでは Microsoft Agent Framework の主要な概念をカバーしています。より複雑なエージェントを構築する際に検討すべき高度なパターンをいくつか紹介します：

- <strong>ミドルウェアの合成</strong>：関数ミドルウェアとチャットミドルウェアを使い、複数のミドルウェアハンドラー（ロギング、認証、レート制限）をチェーンしてエージェントの挙動を細かく制御します。
- <strong>ワークフローチェックポイント</strong>：ワークフローイベントとシリアライズを使い、長時間実行するエージェントプロセスの保存と再開を実装します。
- <strong>動的ツール選択</strong>：ツール記述に対するRAGとMAFのツール登録を組み合わせ、クエリごとに関連性のあるツールだけを提示します。
- <strong>マルチエージェントの引き継ぎ</strong>：ワークフローエッジと条件付きルーティングを使い、専門特化したエージェント間の引き継ぎをオーケストレーションします。

## Microsoft Foundryでの LangChain / LangGraph エージェントのホスティング

Microsoft Agent Framework は <strong>フレームワーク互換性があり</strong>、MAF で書かれたエージェントに限定されません。既に **LangChain** または **LangGraph** で構築されたエージェントがあれば、それを **Microsoft Foundry ホストエージェント** として実行可能で、Foundry がランタイム、セッション、スケーリング、ID、およびプロトコルエンドポイントを管理し、エージェントロジックは LangGraph に保持されます。

これは `langchain_azure_ai.agents.hosting` パッケージを使って実現されており、Foundry ホストエージェントが使用する同じプロトコル上でコンパイルされた LangGraph グラフを公開します。

**1. ホスティングの追加インストール：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` エクストラは Foundry のプロトコルライブラリをインストールします：`azure-ai-agentserver-responses`（OpenAI 互換の `/responses` エンドポイント）と `azure-ai-agentserver-invocations`（汎用の `/invocations` エンドポイント）。

**2. ホスティングプロトコルを選択：**

| プロトコル | ホストクラス | エンドポイント | 使用シーン |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI 互換のチャット、ストリーミング、レスポンス履歴、会話スレッドを使いたい場合 — 会話型エージェントの推奨デフォルト。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | 独自の JSON 形式、Webhook スタイルのエンドポイント、非会話型処理が必要な場合。 |

**Responses API は Foundry でのエージェント開発の主要 API なので**、ほとんどのエージェントは `ResponsesHostServer` から始めることを推奨します。

**3. 環境変数を設定**（事前に `az login` を行い `DefaultAzureCredential` の認証を可能にします）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

エージェントが後で Foundry のホストエージェントとして実行される際は、プラットフォームが自動的に `FOUNDRY_PROJECT_ENDPOINT` を注入します。

**4. Responses プロトコルで LangGraph エージェントを公開：**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAIはFoundryプロジェクトのOpenAI互換（Responses）エンドポイントを対象としています。
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

ローカルで `python main.py` を実行し、`http://localhost:8088/responses` に Responses リクエストを送信します。

**主な挙動：**

- <strong>会話</strong>：クライアントは `previous_response_id` または `conversation` ID を渡すことで会話を継続可能。グラフが LangGraph チェックポインタでコンパイルされていれば、Foundry は会話状態をチェックポイントに紐づけます（本番では永続的なチェックポインタを使用すべきです。ローカルテストには `MemorySaver` で十分です）。
- <strong>ヒューマンインザループ</strong>：グラフが LangGraph の `interrupt()` を使用する場合、`ResponsesHostServer` は保留中の割込みを Responses の `function_call` / `mcp_approval_request` 項目として表現し、クライアントは一致する `function_call_output` / `mcp_approval_response` で再開します。
- **Foundry へのデプロイ**：Azure Developer CLI を使って — `azd ext install azure.ai.agents`、`azd ai agent init -m <manifest>`、`azd ai agent run`（ローカル、Docker 必須）、続いて `azd provision` と `azd deploy`。ホストエージェントのデプロイには **Foundry Project Manager** ロールが必要です。

この例の実行可能なバージョンは [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) にあります。完全なチュートリアル（Invocations プロトコル、カスタムリクエストスキーマ、トラブルシューティング）は [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) を参照してください。

## コードサンプル

Microsoft Agent Framework のコードサンプルはこのリポジトリの `xx-python-agent-framework` と `xx-dotnet-agent-framework` ファイルにあります。

## Microsoft Agent Framework に関する質問は？

他の学習者と会い、オフィスアワーに参加し、AI エージェントの質問に答えてもらうには [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) に参加しましょう。
## 前のレッスン

[AI エージェントのメモリ](../13-agent-memory/README.md)

## 次のレッスン


[コンピューター使用エージェント (CUA) の構築](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->