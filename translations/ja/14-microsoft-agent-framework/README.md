# Microsoft Agent Frameworkの探求

![Agent Framework](../../../translated_images/ja/lesson-14-thumbnail.90df0065b9d234ee.webp)

### はじめに

このレッスンでは以下について説明します：

- Microsoft Agent Frameworkの理解：主な特徴と価値  
- Microsoft Agent Frameworkの主要概念の探求
- 高度なMAFパターン：ワークフロー、ミドルウェア、メモリ

## 学習目標

このレッスンを終えると、以下ができるようになります：

- Microsoft Agent Frameworkを使って本番環境対応のAIエージェントを構築する
- Microsoft Agent Frameworkのコア機能をエージェント利用ケースに適用する
- ワークフロー、ミドルウェア、可観測性を含む高度なパターンを使用する

## コードサンプル 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) のコードサンプルは、このリポジトリの `xx-python-agent-framework` と `xx-dotnet-agent-framework` ファイルで見つけることができます。

## Microsoft Agent Frameworkの理解

![Framework Intro](../../../translated_images/ja/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) は、AIエージェントを構築するためのマイクロソフトの統合フレームワークです。これは、本番環境と研究環境の両方で見られる様々なエージェント利用ケースに対応できる柔軟性を提供します。例えば：

- <strong>逐次的エージェントオーケストレーション</strong>：段階的なワークフローが必要なシナリオ。
- <strong>並行オーケストレーション</strong>：エージェントが同時にタスクを完了する必要があるシナリオ。
- <strong>グループチャットオーケストレーション</strong>：エージェントが一つのタスクに協力して取り組むシナリオ。
- <strong>ハンドオフオーケストレーション</strong>：サブタスクが完了するごとにエージェントがタスクを引き継ぐシナリオ。
- <strong>マグネティックオーケストレーション</strong>：マネージャーエージェントがタスクリストを作成・修正し、サブエージェントの調整を行うシナリオ。

AIエージェントを本番環境で提供するために、MAFは以下の機能も備えています：

- <strong>可観測性</strong>：OpenTelemetryを利用し、AIエージェントのすべてのアクション（ツール呼び出し、オーケストレーションステップ、推論の流れ、Microsoft Foundryのダッシュボードを通じたパフォーマンス監視）を追跡。
- <strong>セキュリティ</strong>：Microsoft Foundryでエージェントをネイティブにホスティングし、役割ベースのアクセス、プライベートデータ処理、組み込みコンテンツ安全機能などのセキュリティ制御を提供。
- <strong>耐久性</strong>：エージェントスレッドやワークフローを一時停止、再開、エラーから回復可能にし、長時間実行プロセスを可能に。
- <strong>制御</strong>：人間が介在するワークフローをサポートし、承認を必要とするタスクをマーク可能。

Microsoft Agent Frameworkは、相互運用性にも注力しています：

- <strong>クラウドに依存しない</strong> - エージェントはコンテナ、オンプレミス、複数のクラウドで動作可能。
- <strong>プロバイダーに依存しない</strong> - Azure OpenAIやOpenAIなど、好みのSDKでエージェントを作成可能。
- <strong>オープンスタンダードの統合</strong> - Agent-to-Agent(A2A)やModel Context Protocol（MCP）などのプロトコルを利用して他エージェントやツールを検出し利用可能。
- <strong>プラグインとコネクタ</strong> - Microsoft Fabric、SharePoint、Pinecone、Qdrantなどのデータ・メモリサービスに接続可能。

これらの機能がMicrosoft Agent Frameworkの主要概念にどのように適用されるかを見てみましょう。

## Microsoft Agent Frameworkの主要概念

### エージェント

![Agent Framework](../../../translated_images/ja/agent-components.410a06daf87b4fef.webp)

<strong>エージェントの作成</strong>

エージェントの作成は、推論サービス（LLMプロバイダー）、
AIエージェントが従う命令セット、そして割り当てられた `name` を定義することで行います：


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上記は `Azure OpenAI` を使用していますが、エージェントは `Microsoft Foundry Agent Service` を含むさまざまなサービスを使用して作成できます：

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

または大きなコンテキストウィンドウ（最大204Kトークン）を備えたOpenAI互換APIを提供する [MiniMax](https://platform.minimaxi.com/)：

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

または A2A プロトコルを利用したリモートエージェント：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

<strong>エージェントの実行</strong>

エージェントはストリーミング応答か非ストリーミング応答かに応じて、`.run` または `.run_stream` メソッドを使って実行されます。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

各エージェントの実行には、エージェントが使用する `max_tokens`、エージェントが呼び出せる `tools`、さらにはエージェントに使われる `model` など、パラメータをカスタマイズするオプションを指定できます。

これは、ユーザーのタスクを完了するために特定のモデルやツールが必要な場合に便利です。

<strong>ツール</strong>

ツールはエージェントを定義するときにも定義できます：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgentを直接作成するとき

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

また、エージェントを実行するときにも定義できます：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # この実行専用のツールです )
```

<strong>エージェントスレッド</strong>

エージェントスレッドはマルチターンの会話を処理するために使われます。スレッドは次のいずれかで作成できます：

- 時間をかけてスレッドを保存できる `get_new_thread()` を使う
- エージェント実行時にスレッドを自動的に作成し、現在の実行中のみスレッドを持続させる

スレッドを作成するコードは次のようになります：

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() # スレッドでエージェントを実行します。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

その後、スレッドをシリアライズして後で保存することができます：

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

エージェントはツールやLLMと連携してユーザーのタスクを完了します。特定のシナリオではこれらのやり取りの間に処理や追跡を行いたい場合があります。エージェントミドルウェアはこれを可能にします：

<em>関数ミドルウェア</em>

このミドルウェアはエージェントと呼び出す関数やツールの間で処理を実行します。たとえば、関数呼び出しのログを取りたい場合に使われます。

下のコードで `next` は次のミドルウェアか実際の関数を呼ぶかを定義しています。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 前処理：関数実行前のログ
    print(f"[Function] Calling {context.function.name}")

    # 次のミドルウェアまたは関数実行へ続行
    await next(context)

    # 後処理：関数実行後のログ
    print(f"[Function] {context.function.name} completed")
```

<em>チャットミドルウェア</em>

このミドルウェアはエージェントとLLMとの間のリクエストに対して処理を実行したりログを取ったりします。

ここにはAIサービスに送信される `messages` などの重要な情報が含まれています。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 前処理: AI呼び出し前のログ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 次のミドルウェアまたはAIサービスへ進む
    await next(context)

    # 後処理: AI応答後のログ
    print("[Chat] AI response received")

```

<strong>エージェントメモリ</strong>

`Agentic Memory` レッスンでも説明したように、メモリはエージェントが異なるコンテキストで動作できるようにする重要な要素です。MAFは複数の種類のメモリを提供します：

<em>インメモリストレージ</em>

これはアプリケーションの実行時にスレッド内に保存されるメモリです。

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() # スレッドでエージェントを実行します。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

<em>永続メッセージ</em>

これは異なるセッション間で会話履歴を保存するのに使われます。`chat_message_store_factory` を使って定義されます：

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

これはエージェント実行前にコンテキストに追加されるメモリです。mem0などの外部サービスに保存可能です：

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


オブザーバビリティは信頼性が高くメンテナブルなエージェントシステムを構築するうえで重要です。MAFはOpenTelemetryと統合して、より良いオブザーバビリティのためのトレーシングやメーターを提供します。

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

MAFは、タスクを完了するための事前定義されたステップであり、それらのステップの構成要素としてAIエージェントを含むワークフローを提供します。

ワークフローはさまざまなコンポーネントで構成されており、制御フローの改善を可能にします。ワークフローはまた、<strong>マルチエージェントオーケストレーション</strong>とワークフロー状態を保存する<strong>チェックポイント</strong>も可能にします。

ワークフローの主要なコンポーネントは次のとおりです：

<strong>エグゼキューター</strong>

エグゼキューターは入力メッセージを受け取り、割り当てられたタスクを実行し、出力メッセージを生成します。これによりワークフローはより大きなタスクの完了に向かって進みます。エグゼキューターはAIエージェントまたはカスタムロジックのいずれかです。

<strong>エッジ</strong>

エッジはワークフロー内のメッセージの流れを定義するために使用されます。次のようなものがあります：

<em>ダイレクトエッジ</em> - エグゼキューター間の単純な一対一の接続：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

<em>条件付きエッジ</em> - 特定の条件が満たされた後に有効になるもの。例えば、ホテルの部屋が利用できない場合、エグゼキューターは他のオプションを提案できます。

<em>スイッチケースエッジ</em> - 定義された条件に基づいてメッセージを異なるエグゼキューターにルーティングします。例えば、旅行顧客に優先アクセスがある場合、そのタスクは別のワークフローで処理されます。

<em>ファンアウトエッジ</em> - 1つのメッセージを複数のターゲットに送信します。

<em>ファンインエッジ</em> - 複数のエグゼキューターからのメッセージを収集して1つのターゲットに送信します。

<strong>イベント</strong>

ワークフローのオブザーバビリティを改善するために、MAFは実行に関する組み込みイベントを提供します：

- `WorkflowStartedEvent`  - ワークフローの実行開始
- `WorkflowOutputEvent` - ワークフローが出力を生成
- `WorkflowErrorEvent` - ワークフローがエラーに遭遇
- `ExecutorInvokeEvent`  - エグゼキューターが処理を開始
- `ExecutorCompleteEvent`  - エグゼキューターが処理を完了
- `RequestInfoEvent` - リクエストが発行される

## 高度なMAFパターン

上記のセクションはMicrosoft Agent Frameworkの基本概念をカバーしています。より複雑なエージェントを構築する際に考慮すべき高度なパターンは以下の通りです：

- <strong>ミドルウェアの合成</strong>：エージェントの動作を細かく制御するために、関数とチャットミドルウェアを使って複数のミドルウェアハンドラー（ロギング、認証、レート制限）を連鎖させます。
- <strong>ワークフローチェックポイント</strong>：ワークフローイベントとシリアル化を利用して、長時間実行されるエージェントプロセスを保存し、再開します。
- <strong>動的ツール選択</strong>：ツールの説明に対するRAGとMAFのツール登録を組み合わせて、クエリごとに関連するツールのみを提示します。
- <strong>マルチエージェントの引き継ぎ</strong>：ワークフローのエッジと条件付きルーティングを使って、専門エージェント間の引き継ぎをオーケストレーションします。

## Microsoft FoundryでのLangChain / LangGraphエージェントのホスティング

Microsoft Agent Frameworkは<strong>フレームワーク間の相互運用性</strong>があり、MAFで書かれたエージェントに限定されません。すでに<strong>LangChain</strong>または<strong>LangGraph</strong>で構築されたエージェントをお持ちの場合、それを<strong>Microsoft Foundryホストエージェント</strong>として実行可能であり、Foundryがランタイム、セッション、スケーリング、ID管理、プロトコルエンドポイントを管理する一方で、エージェントのロジックはLangGraphに維持されます。

これは`langchain_azure_ai.agents.hosting`パッケージを使用して実現されており、Foundryホストエージェントが使用するのと同じプロトコルでコンパイル済みのLangGraphグラフを公開します。

**1. ホスティング用のエクストラをインストールします：**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting`エクストラはFoundryプロトコルライブラリをインストールします：`azure-ai-agentserver-responses`（OpenAI互換の`/responses`エンドポイント）と`azure-ai-agentserver-invocations`（汎用の`/invocations`エンドポイント）。

**2. ホスティングプロトコルを選択します：**

| プロトコル | ホストクラス | エンドポイント | 使用する状況 |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI互換のチャット、ストリーミング、応答履歴、会話スレッドを利用したい場合 — 会話型エージェントに推奨されるデフォルトです。 |
| **Invocations** | `InvocationsHostServer` | `/invocations` | カスタムJSON形式やWebhookスタイルのエンドポイント、または非会話型処理が必要な場合。 |

Foundryにおけるエージェント開発の主なAPIは<strong>Responses API</strong>であるため、ほとんどのエージェントは`ResponsesHostServer`から始めてください。

**3. 環境変数を設定します**（`az login`を先にして`DefaultAzureCredential`が認証できるようにします）：

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

後でエージェントがFoundryでホストエージェントとして実行される際には、プラットフォームが自動的に`FOUNDRY_PROJECT_ENDPOINT`を注入します。

**4. LangGraphエージェントをResponsesプロトコルで公開する：**

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

    # ChatOpenAI ここでは Foundry プロジェクトの OpenAI 互換（Responses）エンドポイントを対象としています。
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

ローカルで`python main.py`で実行し、`http://localhost:8088/responses`にResponsesリクエストを送信します。

**主な動作：**

- <strong>会話の継続</strong>: クライアントは`previous_response_id`または`conversation` IDを渡すことで会話を継続します。グラフがLangGraphのチェックポインターでコンパイルされている場合、Foundryは会話状態をチェックポイントに関連付けます（本番環境では耐久性のあるチェックポインターを使用し、ローカルテストには`MemorySaver`で十分です）。
- <strong>ヒューマンインザループ</strong>: グラフがLangGraphの`interrupt()`を使用している場合、`ResponsesHostServer`は保留中の割り込みをResponsesの`function_call` / `mcp_approval_request`アイテムとして表面化し、クライアントは対応する`function_call_output` / `mcp_approval_response`で再開します。
- **Foundryへのデプロイ**: Azure Developer CLIを使用します— `azd ext install azure.ai.agents`、`azd ai agent init -m <manifest>`、`azd ai agent run`（ローカル、Docker必須）、その後`azd provision`および`azd deploy`。ホストエージェントのデプロイには<strong>Foundry Project Manager</strong>ロールが必要です。

この例は[code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)に実際に動作するバージョンがあります。完全な手順（Invocationsプロトコル、カスタムリクエストスキーマ、トラブルシューティング）については[Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)をご覧ください。

## コードサンプル 

Microsoft Agent Frameworkのコードサンプルはこのリポジトリの`xx-python-agent-framework`と`xx-dotnet-agent-framework`のファイルで見つけられます。

## Microsoft Agent Frameworkについてさらに質問がありますか？

他の学習者と交流し、オフィスアワーに参加し、AIエージェントの質問に答えてもらうには[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)に参加してください。
## 前のレッスン

[AIエージェントのメモリ](../13-agent-memory/README.md)

## 次のレッスン

[コンピュータ利用エージェント（CUA）の構築](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
