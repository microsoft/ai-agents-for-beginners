# Microsoft Agent Framework Workflowを使ったマルチエージェントアプリケーションの構築

このチュートリアルでは、Microsoft Agent Frameworkを使用してマルチエージェントアプリケーションを理解し構築する方法を説明します。マルチエージェントシステムの基本概念を探り、フレームワークのWorkflowコンポーネントのアーキテクチャを詳しく解説し、Pythonと.NETでの実践的な例を通じてさまざまなワークフローパターンを学びます。

## 1\. マルチエージェントシステムの理解

AIエージェントは、通常の大規模言語モデル（LLM）の能力を超えたシステムです。環境を認識し、意思決定を行い、特定の目標を達成するために行動します。マルチエージェントシステムでは、複数のエージェントが協力して、単一のエージェントでは困難または不可能な問題を解決します。

### 一般的なアプリケーションシナリオ

  * **複雑な問題解決**: 大規模なタスク（例: 会社全体のイベント計画）を、専門エージェント（例: 予算エージェント、物流エージェント、マーケティングエージェント）が処理する小さなサブタスクに分割。
  * **バーチャルアシスタント**: 主なアシスタントエージェントが、スケジュール管理、調査、予約などのタスクを専門エージェントに委任。
  * **自動コンテンツ作成**: 1つのエージェントがコンテンツを作成し、別のエージェントが正確性やトーンを確認し、さらに別のエージェントが公開するワークフロー。

### マルチエージェントパターン

マルチエージェントシステムは、エージェントの相互作用方法を決定するいくつかのパターンで構成できます：

  * **順次型**: エージェントが決められた順序で作業を行い、1つのエージェントの出力が次のエージェントの入力になります。
  * **並行型**: エージェントがタスクの異なる部分を並行して作業し、結果を最後に集約します。
  * **条件型**: エージェントの出力に基づいて異なる経路をたどるワークフロー（if-then-else文のようなもの）。

## 2\. Microsoft Agent Framework Workflowアーキテクチャ

Agent Frameworkのワークフローシステムは、複数のエージェント間の複雑な相互作用を管理するための高度なオーケストレーションエンジンです。これは、同期ステップ「スーパーステップ」で処理が行われる[Pregelスタイルの実行モデル](https://kowshik.github.io/JPregel/pregel_paper.pdf)に基づいたグラフベースのアーキテクチャで構築されています。

### コアコンポーネント

アーキテクチャは以下の3つの主要部分で構成されています：

1. **Executors**: 基本的な処理ユニットです。例では、`Agent`がExecutorの一種です。各Executorは、受信したメッセージの種類に基づいて自動的に呼び出される複数のメッセージハンドラーを持つことができます。
2. **Edges**: Executors間でメッセージが移動する経路を定義します。Edgesには条件を設定でき、ワークフローグラフを動的にルーティングすることが可能です。
3. **Workflow**: 全体のプロセスをオーケストレーションし、Executors、Edges、実行の流れ全体を管理します。メッセージが正しい順序で処理されることを保証し、観測性のためにイベントをストリームします。

*ワークフローシステムのコアコンポーネントを示す図*

この構造により、順次チェーン、並列処理のファンアウト/ファンイン、条件フローのスイッチケースロジックなどの基本的なパターンを使用して、堅牢でスケーラブルなアプリケーションを構築することができます。

## 3\. 実践例とコード分析

次に、フレームワークを使用してさまざまなワークフローパターンを実装する方法を見ていきます。各例についてPythonと.NETのコードを確認します。

### ケース1: 基本的な順次ワークフロー

これは最も簡単なパターンで、1つのエージェントの出力が直接別のエージェントに渡されます。シナリオでは、ホテルの`FrontDesk`エージェントが旅行のおすすめを行い、それを`Concierge`エージェントがレビューします。

*基本的なFrontDesk -> Conciergeワークフローの図*

#### シナリオ背景

旅行者がパリでのおすすめを尋ねます。

1. `FrontDesk`エージェントは簡潔さを重視し、ルーブル美術館を訪れることを提案します。
2. `Concierge`エージェントは本格的な体験を優先し、この提案をレビューして、より地元らしい観光地を提案します。

#### Python実装分析

Pythonの例では、まず2つのエージェントを定義して作成します。それぞれに特定の指示を与えます。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

次に、`WorkflowBuilder`を使用してグラフを構築します。`front_desk_agent`を開始ポイントとして設定し、その出力を`reviewer_agent`に接続するエッジを作成します。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

最後に、初期ユーザープロンプトでワークフローを実行します。

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) 実装分析

.NETの実装も非常に似たロジックに従います。まず、エージェントの名前と指示の定数を定義します。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

エージェントは`OpenAIClient`を使用して作成され、`WorkflowBuilder`で`frontDeskAgent`から`reviewerAgent`への順次フローを定義します。

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

その後、ユーザーのメッセージでワークフローを実行し、結果をストリームで返します。

### ケース2: マルチステップ順次ワークフロー

このパターンは基本的な順次型を拡張し、より多くのエージェントを含めます。複数段階の精査や変換が必要なプロセスに最適です。

#### シナリオ背景

ユーザーがリビングルームの画像を提供し、家具の見積もりを依頼します。

1. **Sales-Agent**: 画像内の家具アイテムを特定し、リストを作成します。
2. **Price-Agent**: アイテムリストを受け取り、予算、中価格帯、高価格帯のオプションを含む詳細な価格内訳を提供します。
3. **Quote-Agent**: 価格付きリストを受け取り、Markdown形式の正式な見積書にフォーマットします。

*Sales -> Price -> Quoteワークフローの図*

#### Python実装分析

3つのエージェントが定義され、それぞれが専門的な役割を持ちます。ワークフローは`add_edge`を使用してチェーンを作成します：`sales_agent` -> `price_agent` -> `quote_agent`。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

入力はテキストと画像URIを含む`ChatMessage`です。フレームワークは各エージェントの出力を次のエージェントに渡し、最終的な見積もりを生成します。

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C#) 実装分析

.NETの例もPythonバージョンを反映しています。3つのエージェント（`salesagent`、`priceagent`、`quoteagent`）が作成されます。`WorkflowBuilder`はそれらを順次リンクします。

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ユーザーのメッセージは画像データ（バイト形式）とテキストプロンプトを含む形で構築されます。`InProcessExecution.StreamAsync`メソッドがワークフローを開始し、最終出力がストリームから取得されます。

### ケース3: 並行ワークフロー

このパターンは、タスクを同時に実行して時間を節約する場合に使用されます。複数のエージェントへの「ファンアウト」と結果を集約する「ファンイン」を含みます。

#### シナリオ背景

ユーザーがシアトル旅行の計画を依頼します。

1. **Dispatcher (ファンアウト)**: ユーザーのリクエストが同時に2つのエージェントに送信されます。
2. **Researcher-Agent**: シアトルの観光地、天気、12月の旅行における重要な考慮事項を調査します。
3. **Plan-Agent**: 独立して詳細な日ごとの旅行日程を作成します。
4. **Aggregator (ファンイン)**: リサーチャーとプランナーの出力を収集し、最終結果としてまとめて提示します。

*並行型ResearcherとPlannerワークフローの図*

#### Python実装分析

`ConcurrentBuilder`を使用すると、このパターンの作成が簡単になります。参加するエージェントをリストするだけで、ビルダーが必要なファンアウトとファンインロジックを自動的に作成します。

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

フレームワークは`research_agent`と`plan_agent`が並行して実行されることを保証し、最終出力をリストに集約します。

#### .NET (C#) 実装分析

.NETでは、このパターンはより明示的な定義が必要です。カスタムExecutor（`ConcurrentStartExecutor`と`ConcurrentAggregationExecutor`）がファンアウトとファンインロジックを処理するために作成されます。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder`はこれらのカスタムExecutorとエージェントを使用して、`AddFanOutEdge`と`AddFanInEdge`を使ってグラフを構築します。

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ケース4: 条件付きワークフロー

条件付きワークフローは分岐ロジックを導入し、中間結果に基づいて異なる経路を取ることができます。

#### シナリオ背景

このワークフローは技術チュートリアルの作成と公開を自動化します。

1. **Evangelist-Agent**: 提供されたアウトラインとURLに基づいてチュートリアルのドラフトを作成します。
2. **ContentReviewer-Agent**: ドラフトをレビューし、単語数が200語を超えているかどうかを確認します。
3. **条件分岐**:
      * **承認（`Yes`）の場合**: ワークフローは`Publisher-Agent`に進みます。
      * **拒否（`No`）の場合**: ワークフローは停止し、拒否理由を出力します。
4. **Publisher-Agent**: ドラフトが承認された場合、このエージェントがコンテンツをMarkdownファイルに保存します。

#### Python実装分析

この例では、条件ロジックを実装するためにカスタム関数`select_targets`を使用します。この関数は`add_multi_selection_edge_group`に渡され、`review_result`フィールドに基づいてワークフローを指示します。

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

カスタムExecutor（例: `to_reviewer_result`）は、エージェントのJSON出力を解析し、選択関数が検査できる強く型付けされたオブジェクトに変換します。

#### .NET (C#) 実装分析

.NETバージョンでは、条件関数を使用して同様のアプローチを取ります。`Func<object?, bool>`が定義され、`ReviewResult`オブジェクトの`Result`プロパティをチェックします。

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge`メソッドの`condition`パラメータを使用して、`WorkflowBuilder`が分岐パスを作成します。ワークフローは`GetCondition(expectedResult: "Yes")`がtrueを返す場合のみ`publishExecutor`へのエッジをたどります。それ以外の場合は`sendReviewerExecutor`へのパスをたどります。

## 結論

Microsoft Agent Framework Workflowは、複雑なマルチエージェントシステムをオーケストレーションするための堅牢で柔軟な基盤を提供します。そのグラフベースのアーキテクチャとコアコンポーネントを活用することで、開発者はPythonと.NETで洗練されたワークフローを設計および実装できます。アプリケーションが単純な順次処理、並列実行、または動的な条件ロジックを必要とする場合でも、フレームワークは強力でスケーラブル、かつ型安全なAI駆動ソリューションを構築するためのツールを提供します。

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。