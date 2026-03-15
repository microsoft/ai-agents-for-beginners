# Microsoft Agent Framework の探求

![Agent Framework](../../../translated_images/ja/lesson-14-thumbnail.90df0065b9d234ee.webp)

### はじめに

このレッスンでは以下をカバーします：

- Microsoft Agent Framework の理解：主な機能と価値  
- Microsoft Agent Framework の主要概念の探求
- 高度な MAF パターン：ワークフロー、ミドルウェア、およびメモリ

## 学習目標

このレッスンを完了すると、以下のことができるようになります：

- Microsoft Agent Framework を使用して本番環境向けの AI エージェントを構築する
- Microsoft Agent Framework のコア機能をエージェント利用ケースに適用する
- ワークフロー、ミドルウェア、オブザーバビリティを含む高度なパターンを使用する

## コードサンプル 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) のコードサンプルは、このリポジトリの `xx-python-agent-framework` および `xx-dotnet-agent-framework` ファイルにあります。

## Microsoft Agent Framework の理解

![Framework Intro](../../../translated_images/ja/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) は AI エージェント構築のための Microsoft の統合フレームワークです。実運用や研究環境で見られるさまざまなエージェント利用ケースに対応する柔軟性を提供します。例として：

- **逐次エージェントオーケストレーション**：ステップバイステップのワークフローが必要なシナリオ
- **同時並行オーケストレーション**：エージェントが同時にタスクを完了する必要があるシナリオ
- **グループチャットオーケストレーション**：複数のエージェントが１つのタスクに協力するシナリオ
- **ハンドオフオーケストレーション**：サブタスクが完了するとエージェント間でタスクを引き継ぐシナリオ
- **マグネティックオーケストレーション**：マネージャーエージェントがタスクリストを作成・変更し、サブエージェントを調整してタスクを完了するシナリオ

本番環境で AI エージェントを提供するため、MAF には以下の機能も組み込まれています：

- **オブザーバビリティ**：OpenTelemetry を使用し、AI エージェントのあらゆる行動（ツール呼び出し、オーケストレーションステップ、推論フロー、パフォーマンス監視）を Microsoft Foundry ダッシュボードで監視可能
- **セキュリティ**：Microsoft Foundry 上でエージェントをネイティブホストし、役割ベースアクセス、プライベートデータ処理、組み込みコンテンツセーフティなどのセキュリティ制御を含む
- **耐久性**：エージェントスレッドとワークフローは一時停止、再開、エラーからの回復が可能で、長時間実行されるプロセスに対応
- **コントロール**：人間が介在するフローもサポートし、タスクが人間の承認を必要とする場合に対応可能

Microsoft Agent Framework はまた、相互運用性にも重点を置いています：

- **クラウド非依存** - エージェントはコンテナ、オンプレミス、複数クラウドで実行可能
- **プロバイダー非依存** - Azure OpenAI や OpenAI など任意の SDK でエージェントを作成可能
- **オープンスタンダード統合** - Agent-to-Agent (A2A)、Model Context Protocol (MCP) などのプロトコルで他のエージェントやツールを発見・利用可能
- **プラグインとコネクタ** - Microsoft Fabric、SharePoint、Pinecone、Qdrant などのデータ・メモリサービスに接続可能

これらの機能が Microsoft Agent Framework の主要概念にどのように適用されているかを見てみましょう。

## Microsoft Agent Framework の主要概念

### エージェント

![Agent Framework](../../../translated_images/ja/agent-components.410a06daf87b4fef.webp)

**エージェントの作成**

エージェント作成は、推論サービス（LLM プロバイダー）、エージェントが従う指示セット、および割り当てられた `name` を定義することで行います：

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

上記は `Azure OpenAI` を使用していますが、エージェントは `Microsoft Foundry Agent Service` など多様なサービスを使って作成可能です：

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

または A2A プロトコルを使ったリモートエージェント：

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**エージェントの実行**

エージェントは `.run` または `.run_stream` メソッドを用いて、非ストリーミングまたはストリーミングレスポンスで実行されます。

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

各エージェント実行では、`max_tokens`（エージェントが利用する最大トークン数）、呼び出せる `tools`、さらにはエージェントに使用される `model` 自体などのパラメーターをカスタマイズできます。

これはユーザーのタスク完了に特定のモデルやツールが必要な場合に有効です。

**ツール**

ツールはエージェント定義時に設定可能です：

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgentを直接作成する場合

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

また、エージェント実行時にも設定可能です：

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # この実行のためだけに提供されたツール )
```

**エージェントスレッド**

エージェントスレッドはマルチターン会話を処理するために使用されます。スレッドは以下のいずれかで作成できます：

- 時間をかけてスレッドを保存可能にする `get_new_thread()` の使用
- 実行時に自動的にスレッドを作成し、その実行中のみ有効にする方法

スレッド作成コード例：

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() # スレッドでエージェントを実行します。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

後から使用するためにスレッドをシリアライズして保存することも可能：

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() 

# スレッドでエージェントを実行します。

response = await agent.run("Hello, how are you?", thread=thread) 

# ストレージのためにスレッドをシリアライズします。

serialized_thread = await thread.serialize() 

# ストレージからの読み込み後にスレッド状態をデシリアライズします。

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**エージェントミドルウェア**

エージェントはユーザーのタスクを完了するためにツールや LLM と連携します。特定のシナリオでは、そのやり取りの間で処理や追跡を実行したい場合があります。エージェントミドルウェアはこれを可能にします：

*Function Middleware*

このミドルウェアは、エージェントと呼び出す関数／ツール間でアクションを実行できます。たとえば関数呼び出しのログ記録に使用されます。

以下のコードの `next` は、次のミドルウェアか実際の関数のいずれかを呼び出すことを定義します。

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # 前処理：関数実行前にログを記録
    print(f"[Function] Calling {context.function.name}")

    # 次のミドルウェアまたは関数実行に進む
    await next(context)

    # 後処理：関数実行後にログを記録
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

このミドルウェアは、エージェントと LLM との間のリクエストでアクションの実行やログ記録を可能にします。

ここには AI サービスに送られる `messages` など重要な情報が含まれます。

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # 前処理: AI呼び出し前のログ
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # 次のミドルウェアまたはAIサービスへ続行
    await next(context)

    # 後処理: AI応答後のログ
    print("[Chat] AI response received")

```

**エージェントメモリ**

「Agentic Memory」レッスンで取り上げたように、メモリは異なるコンテキストでエージェントを動作させるための重要な要素です。MAF はいくつかの種類のメモリを提供しています：

*インメモリストレージ*

これはアプリの実行中にスレッド内に保存されるメモリです。

```python
# 新しいスレッドを作成します。
thread = agent.get_new_thread() # スレッドでエージェントを実行します。
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*永続的メッセージ*

これは異なるセッション間で会話履歴を保存するためのメモリで、`chat_message_store_factory` で定義されます：

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

*ダイナミックメモリ*

これはエージェント実行前にコンテキストに追加されるメモリで、mem0 のような外部サービスに保存可能です：

```python
from agent_framework.mem0 import Mem0Provider

# 高度なメモリ機能のためにMem0を使用しています
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

**エージェントオブザーバビリティ**

オブザーバビリティは信頼性の高い保守可能なエージェントシステム構築に重要です。MAF は OpenTelemetry と統合し、トレースやメーターを提供して優れた可観測性を実現しています。

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

MAF はタスク完了のための事前定義されたステップであるワークフローを提供し、これらのステップに AI エージェントをコンポーネントとして含めます。

ワークフローは異なるコンポーネントからなり、制御フローの管理を向上します。ワークフローは **マルチエージェントオーケストレーション** と **チェックポイント** によるワークフロー状態の保存も可能にします。

ワークフローの主要コンポーネントは：

**エグゼキューター**

エグゼキューターは入力メッセージを受け取り、割り当てられたタスクを実行し、その後出力メッセージを生成します。これによりワークフローは大きなタスクを完了に向けて進みます。エグゼキューターは AI エージェントまたはカスタムロジックのいずれかです。

**エッジ**

エッジはワークフロー内のメッセージのフローを定義します。次のようなタイプがあります：

*ダイレクトエッジ* — エグゼキューター間の単純な一対一接続：

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*条件付きエッジ* — 特定条件を満たした時に有効化。例えばホテルの部屋が無い場合、他のオプションを提案できます。

*スイッチケースエッジ* — 定義された条件によってメッセージを異なるエグゼキューターにルーティング。例：旅行顧客に優先アクセス権がある場合、タスクが別のワークフローで処理される。

*ファンアウトエッジ* — １つのメッセージを複数のターゲットに送信。

*ファンインエッジ* — 複数のエグゼキューターからのメッセージを収集し、１つのターゲットに送信。

**イベント**

ワークフローのより良い可視化のために、MAF は実行に関するビルトインイベントを提供しています：

- `WorkflowStartedEvent`  - ワークフロー実行開始
- `WorkflowOutputEvent` - ワークフローが出力を生成
- `WorkflowErrorEvent` - ワークフローがエラーに遭遇
- `ExecutorInvokeEvent`  - エグゼキューターの処理開始
- `ExecutorCompleteEvent`  -  エグゼキューターの処理完了
- `RequestInfoEvent` - リクエスト発行

## 高度な MAF パターン

前述のセクションは Microsoft Agent Framework の主要概念をカバーしています。より複雑なエージェントを構築する際は、次の高度なパターンを考慮してください：

- **ミドルウェアの合成**：関数ミドルウェアおよびチャットミドルウェアを用いて複数のミドルウェアハンドラー（ログ、認証、レート制限）をチェーンし、エージェントの挙動を細かく制御
- **ワークフローチェックポイント**：ワークフローイベントとシリアライズを活用し、長期実行エージェントプロセスの保存と再開が可能
- **ダイナミックツール選択**：ツールの説明上での RAG と MAF のツール登録を組み合わせ、クエリごとに関連するツールのみを提示
- **マルチエージェントハンドオフ**：ワークフローのエッジと条件付きルーティングを用いて、専門化されたエージェント間のハンドオフをオーケストレーション

## コードサンプル 

Microsoft Agent Framework のコードサンプルは、このリポジトリの `xx-python-agent-framework` および `xx-dotnet-agent-framework` ファイルにあります。

## Microsoft Agent Framework についてさらに質問がありますか？

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) に参加して、他の学習者と交流したり、オフィスアワーに参加して AI エージェントに関する質問を解決しましょう。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の確保に努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。原本の言語による文書を正本としてご参照ください。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の使用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->